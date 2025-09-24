from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic")
]

# No data validation in structured output parser
# If you want data validation, use PydanticOutputParser instead
parser = StructuredOutputParser.from_response_schemas(schema)
template  = PromptTemplate(
    template="Give me 3 interesting facts about {topic}.\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({"topic": "SpaceX"})
print(result)
# Alternatively, you can invoke each step separately:
# prompt = template.invoke({"topic": "SpaceX"})
# response = model.invoke(prompt)
# output = parser.parse(response)
# print(output)

