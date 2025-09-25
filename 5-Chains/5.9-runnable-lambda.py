from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

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

def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

# Create the first chain to get the joke
joke_chain = RunnableSequence(prompt1, model, parser)

# Create explanation chain
explanation_chain = RunnableSequence(prompt2, model, parser)

# Create a parallel chain that preserves the joke and adds word count
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),  # Pass the joke through unchanged
    'word_count': runnable_word_counter,  # Count words in the joke
    'explanation': explanation_chain  # Generate explanation from the joke
})

# Create the final chain: generate joke -> parallel processing
final_chain = RunnableSequence(joke_chain, parallel_chain)
result = final_chain.invoke({'topic': 'cricket'})

# Print all results
print("JOKE:")
print(result['joke'])
print(f"\nWORD COUNT: {result['word_count']}")
print("\nEXPLANATION:")
print(result['explanation'])