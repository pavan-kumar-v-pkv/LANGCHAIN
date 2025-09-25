from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template= 'Write a joke about {topic}.',
    input_variables=['topic'],
)
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke in a simple way:\n\n{joke}',
    input_variables=['joke'],
)

# Create the first chain to get the joke
joke_chain = RunnableSequence(prompt1, model, parser)
joke_result = joke_chain.invoke({'topic': 'cats'})

# Create the explanation chain
explanation_chain = RunnableSequence(prompt2, model, parser)
explanation_result = explanation_chain.invoke({'joke': joke_result})

# Print both results
print("JOKE:")
print(joke_result)
print("\nEXPLANATION:")
print(explanation_result)