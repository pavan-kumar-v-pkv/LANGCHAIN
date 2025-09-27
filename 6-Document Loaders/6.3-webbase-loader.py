from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader = WebBaseLoader("https://en.wikipedia.org/wiki/Artificial_intelligence")
docs = loader.load()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
prompt = PromptTemplate(
    template="answer the following question \n {question} from the context below \n {context}",
    input_variables=["question", "context"]
)

parser = StrOutputParser()

print(type(docs))
print(f"Number of documents: {len(docs)}")
print(f"First document content preview: {docs[0].page_content[:200]}...")
print(f"Document metadata: {docs[0].metadata}")

chain = prompt | model | parser
result = chain.invoke({'question': 'What are the techniques used?', 'context': docs[0].page_content})
print("RESULT:")
print(result)