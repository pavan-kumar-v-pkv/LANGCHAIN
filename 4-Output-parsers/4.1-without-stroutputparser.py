from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage

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

prompt1 = template1.invoke({'topic': 'black hole'})
result1 = model.invoke([HumanMessage(content=prompt1.text)])

prompt2 = template2.invoke({'report': result1.content})
result2 = model.invoke([HumanMessage(content=prompt2.text)])

print(result2.content)