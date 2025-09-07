from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearm.metrics.pairwise import cosine_similarity
import numpy as np
import os


# Load .env from parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=300)
documents = [
    "Virat Kohli is a former captain of the Indian cricket team. He is known for his aggressive batting style.",
    "Sachin Tendulkar is known as the 'God of Cricket'. He has scored 100 international centuries.",
    "M.S. Dhoni is a former captain of the Indian cricket team. He is known for his cool demeanor and finishing abilities.",
    "Rohit Sharma is the current captain of the Indian cricket team. He is known for his elegant batting style.",
    "KL Rahul is a prominent Indian cricketer known for his versatility and batting skills."
]
query = "Who is the current captain of the Indian cricket team?"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

similarities = cosine_similarity([query_embedding], doc_embeddings)
index, score = sorted(list(enumerate(similarities[0])), key=lambda x: x[1], reverse=True)[0]
print("Most similar document index:", index)
print("Most similar document score:", score)
print(query)
print(documents[index])