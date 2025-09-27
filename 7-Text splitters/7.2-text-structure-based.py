from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
LangChain is a framework for developing applications powered by language models. It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more.
It enables developers to build applications that are more advanced than those that can be created with a language model alone by providing a standard interface for all LLMs and a selection of integrations with other tools.
"""
# Initialize the text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

# perform the split
chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)