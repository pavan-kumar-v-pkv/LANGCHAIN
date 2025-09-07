from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
# Load .env from parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

model = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)
result = model.embed_query("Delhi is the capital of India")
print(str(result))
