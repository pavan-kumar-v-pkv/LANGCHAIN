from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name and age of a person who lives in {location}.\n {format_instruction}",
    input_variables=["location"],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# Create a chain using the template (not the invoked prompt)
chain = template | model | parser

# Invoke the chain with the input
result = chain.invoke({'location': 'New York'})
print(result)