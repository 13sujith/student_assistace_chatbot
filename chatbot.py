# imports
from transformers import pipeline
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

DB_DIR = "db"

# embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# vector DB
vector_db = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embeddings
)

retriever = vector_db.as_retriever(search_kwargs={"k": 5})

# LLM
hf_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=512
)

llm = HuggingFacePipeline(pipeline=hf_pipeline)

# prompt
prompt = PromptTemplate.from_template(
"""
You are an academic assistant.
Answer ONLY using the given context.


Context:
{context}

Question:
{question}

Answer:
"""
)

# ✅ RAG CHAIN (THIS WAS MISSING OR WRONG)
rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
)

print("✅ RAG Chatbot ready! Type 'quit' to exit.")

while True:
    query = input("Ask: ")
    if query.lower() == "quit":
        break
    response = rag_chain.invoke(query)
    print(response)



