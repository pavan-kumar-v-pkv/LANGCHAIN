from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
prompt = PromptTemplate(
    template="tell in simple words about this {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

loader = TextLoader("Artificial Intelligence (AI).txt") 
docs = loader.load()
print(type(docs))
print(f"Number of documents: {len(docs)}")
print(f"First document content preview: {docs[0].page_content[:200]}...")
print(f"Document metadata: {docs[0].metadata}")

chain = prompt | model | parser
result = chain.invoke({'topic': docs[0].page_content})
print("RESULT:")
print(result)