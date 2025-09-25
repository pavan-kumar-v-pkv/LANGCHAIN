from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatOpenAI(model="gpt-4o-mini", temperature=0)
model2 = ChatGroq(model="mixtral-8x7b-32768", temperature=0)

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text:\n\n{text}",
    input_variables=["text"],
)

prompt2 = PromptTemplate(
    template="Generate 5 short question answers from the following notes:\n\n{text}",
    input_variables=["text"],
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single study guide:\n\nNotes:\n{notes}\n\nQuiz:\n{quiz}",
    input_variables=["notes", "quiz"],
)

parser = StrOutputParser()
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser,
})

merge_chain = prompt3 | model2 | parser
chain = parallel_chain | merge_chain
text = 'Artificial Intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior. It encompasses various subfields, including machine learning, natural language processing, robotics, and computer vision. AI systems can analyze data, recognize patterns, and make decisions with minimal human intervention. The development of AI has led to advancements in numerous industries, such as healthcare, finance, and transportation. However, it also raises ethical concerns regarding privacy, job displacement, and the potential for biased decision-making.'
chain.invoke({'text': text})
print(chain.get_graph().draw_ascii())  # Optional: visualize the chain structure