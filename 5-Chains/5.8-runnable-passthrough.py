from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template= 'Write a joke about {topic}.',
    input_variables=['topic'],
)
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke in a simple way:\n\n{joke}',
    input_variables=['joke'],
)

# Create the first chain to get the joke
joke_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': joke_chain,
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_chain, parallel_chain)
joke_result = final_chain.invoke({'topic': 'cricket'})
# Print both results
print("JOKE:")
print(joke_result['joke'])
print("\nEXPLANATION:")
print(joke_result['explanation'])