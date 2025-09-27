from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("SQL_Interview_Questions_with_Examples.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=""
)

# result = splitter.split_text(text)
result = splitter.split_documents(docs)
print(result[0])