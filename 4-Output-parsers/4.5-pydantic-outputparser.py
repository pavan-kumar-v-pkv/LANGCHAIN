from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person in years")
    city: str = Field(description="City where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Give me the name and age of a person who lives in {location}.\n {format_instruction}",
    input_variables=["location"],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'location': 'Ireland'})
print(result)

# prompt = template.invoke({'location': 'New York'})
# response = model.invoke(prompt)
# output = parser.parse(response.content)  # Extract .content from AIMessage
# print(output)
# print(f"Name: {output.name}, Age: {output.age}, City: {output.city}")