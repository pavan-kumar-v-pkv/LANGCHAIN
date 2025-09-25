from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch

load_dotenv()

prompt1 = PromptTemplate(
    template= 'Write a detailed report on {topic}.',
    input_variables=['topic'],
)
prompt2 = PromptTemplate(
    template='Summarize the following report in a concise manner:\n\n{report}',
    input_variables=['report'],
)

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()

report_chain = RunnableSequence(prompt1, model, parser)
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_chain, branch_chain)
result = final_chain.invoke({'topic': 'Russia vs Ukraine war'})
print(result)
print(final_chain.get_graph().print_ascii())