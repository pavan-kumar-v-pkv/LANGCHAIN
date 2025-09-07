from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 256, "temperature": 0}
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India?")

print(result.content)