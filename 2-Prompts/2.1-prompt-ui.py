from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header("Research Tool")

paper_input = st.selectbox("Select a research paper", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT3: Language Models are Few-Shot Learners", "Diffusion Models Beast GANs on Image Synthesis"])
style_input = st.selectbox("Select explanation style", ["Beginner-Friendly", "Formal", "Informal", "Technical", "Conversational"])
length_input = st.selectbox("Select explanation length", ["Short", "Medium", "Long"])

# template
template = PromptTemplate(
    template="""
    Please summarize the research paper titled '{paper_input}' in a {style_input} style with a {length_input} length.
    Please include key contributions, methodology, results and also Analogies that are relatable to simplify complex ideas.
    If certain information is not available, respond with "I'm sorry, I don't have that information." instead of making up details.
    Ensure the summary is clear, accurate and aligned with the selected style and length.
    """,
    input_variables=["paper_input", "style_input", "length_input"]
)

prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

if st.button("Summarize"):
    # Create a ChatOpenAI instance
    chat_model = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Create a message and invoke the model
    result = chat_model.invoke([HumanMessage(content=prompt.text)])
    
    # Display the result
    st.write(result.content)
