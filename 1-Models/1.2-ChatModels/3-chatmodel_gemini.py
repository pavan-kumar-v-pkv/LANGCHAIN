from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os   
# Load .env from parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0)
result = model.invoke("What is the capital of India?")
print(result.content)