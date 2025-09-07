from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text = "Delhi is the capital of India"
documents = [
    "LangChain is a framework for developing applications powered by language models.",
    "It enables developers to build applications that can understand and generate natural language.",
    "LangChain provides tools for prompt management, memory, and chaining of calls to language models.",
]

result = embedding.embed_documents(documents)
vector = embedding.embed_query(text)
print(str(vector))