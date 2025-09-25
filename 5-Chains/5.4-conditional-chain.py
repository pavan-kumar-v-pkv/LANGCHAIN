from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['Positive', 'Negative'] = Field(description="Sentiment of the feedback")
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following text as Positive or Negative:\n\n{feedback}\n{format_instruction}',
    input_variables=["feedback"],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2
# result = classifier_chain.invoke({'feedback': 'The product quality is excellent and I am very satisfied with my purchase.'})
# # result = classifier_chain.invoke({'feedback': 'The delivery was late and the item was damaged.'})
# print(result)

prompt2 = PromptTemplate(
    template='Write an appropriate response to the following {sentiment} feedback:\n\n{feedback}',
    input_variables=['sentiment', 'feedback'],
)

# Function to transform the output and preserve original feedback
def transform_for_response(x):
    # x is a dict with 'feedback_obj' (Feedback object) and 'original_feedback' (string)
    feedback_obj = x['feedback_obj']
    original_feedback = x['original_feedback']
    return {
        'sentiment': feedback_obj.sentiment,
        'feedback': original_feedback
    }

# Create a transformation chain that preserves original feedback
transform_chain = RunnableLambda(lambda x: {
    'feedback_obj': x['feedback_obj'], 
    'original_feedback': x['original_feedback']
}) | RunnableLambda(transform_for_response)

branch_chain = RunnableBranch(
    (lambda x: x['sentiment'] == 'Positive', prompt2 | model | parser),
    (lambda x: x['sentiment'] == 'Negative', prompt2 | model | parser),
    RunnableLambda(lambda x: 'Could not find sentiment')  # Default case
)

# Modified chain that preserves original feedback
def create_input_with_feedback(input_dict):
    original_feedback = input_dict['feedback']
    classified = classifier_chain.invoke(input_dict)
    return {
        'feedback_obj': classified,
        'original_feedback': original_feedback
    }

chain = RunnableLambda(create_input_with_feedback) | transform_chain | branch_chain
result = chain.invoke({'feedback': 'The product quality is excellent and I am very satisfied with my purchase.'})
# result = chain.invoke({'feedback': 'The delivery was late and the item was damaged.'})
print(result)
print(chain.get_graph().draw_ascii())  # Optional: visualize the chain structure