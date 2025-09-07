from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load .env from parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

model = ChatOpenAI(model='gpt-4', temperature=0, max_completion_tokens=10)
result = model.invoke("What is the capital of India?")
print(result.content)