from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Use OpenAI instead for better reliability
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}.',
    input_variables=['topic']
)
# 2nd prompt -> short summary
template2 = PromptTemplate(
    template='Summarize the following report in 5 sentences:\n\n{report}',
    input_variables=['report']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic': 'global warming'})
print(result)
