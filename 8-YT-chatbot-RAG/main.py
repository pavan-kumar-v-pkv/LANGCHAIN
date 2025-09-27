from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()

# ---- Step 1: Fetch YouTube transcript ----
yt_id = "aircAruvnKk"  # Example: 3Blue1Brown Neural Networks
api = YouTubeTranscriptApi()
transcript_obj = api.fetch(yt_id)
transcript = transcript_obj.snippets
print(f"Transcript fetched with {len(transcript)} segments.")

# Join text
full_text = " ".join([snippet.text for snippet in transcript])

print(f'Full transcript (first 500 chars): {full_text[:500]}')

# ---- Step 2: Split text into chunks ----
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200,
)
docs = splitter.create_documents([full_text])
print(f"Document split into {len(docs)} chunks.")
print(f'Type of docs: {type(docs)}, type of first chunk: {type(docs[0])}, content preview: {docs[0].page_content[:200]}')

# ---- Step 3: Create vector store ----
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs, embeddings)
print(f"Vector store created with {vector_store.index.ntotal} vectors.")

# ---- Step 4: Create conversational retrieval chain ----
memory = ConversationBufferMemory(
    memory_key="chat_history", 
    return_messages=True
)

qa = ConversationalRetrievalChain.from_llm(
    ChatOpenAI(model="gpt-4o-mini", temperature=0),
    retriever=vector_store.as_retriever(),
    memory=memory
)

# ---- Step 5: Chat with the bot ----
print("You can now chat with the bot! Type 'exit' to quit.")
while True:
    query = input("You: ")
    if query.lower() == 'exit':
        break
    response = qa.invoke({"question": query})['answer']
    print(f"Bot: {response}\n")