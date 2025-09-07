from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
# Load .env from parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)
documents = [
    "LangChain is a framework for developing applications powered by language models.",
    "It enables developers to build applications that can understand and generate natural language.",
    "LangChain provides tools for prompt management, memory, and chaining of calls to language models.",
]

result = embedding.embed_documents(documents)
print(str(result))
