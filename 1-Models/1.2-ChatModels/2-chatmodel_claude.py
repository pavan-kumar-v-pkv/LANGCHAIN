from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os   

# Load .env from parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')
result = model.invoke("What is the capital of India?")
print(result.content)