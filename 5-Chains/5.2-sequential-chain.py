from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}.',
    input_variables=['topic'],
)

prompt2 = PromptTemplate(
    template='Summarize the following report in a concise manner mainly in 5 points:\n\n{report}',
    input_variables=['report'],
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({'topic': 'The impact of climate change on global agriculture'})
print(result)
print(chain.get_graph().draw_ascii())  # Optional: visualize the chain structure