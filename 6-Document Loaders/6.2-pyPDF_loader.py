from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

loader = PyPDFLoader("SQL_Interview_Questions_with_Examples.pdf")
docs = loader.load()

print(type(docs))
print(f"Number of documents: {len(docs)}")
print(f"First document content preview: {docs[0].page_content[:200]}...")
print(f"Document metadata: {docs[0].metadata}")