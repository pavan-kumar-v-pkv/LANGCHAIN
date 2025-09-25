from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template = "Generate 5 interesting facts about {topic}.",
    input_variables = ['topic'],
)

model = ChatOpenAI(model_name='gpt-4o-mini', temperature=0)
parser = StrOutputParser()

# Create a chain using the template (not the invoked prompt)
chain = prompt | model | parser
result = chain.invoke({'topic': 'space exploration'})
print(result)

print(chain.get_graph().print_ascii())