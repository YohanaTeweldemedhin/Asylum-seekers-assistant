from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are an AI assistant that helps asylum seekers understand the Dublin Regulation.

Use ONLY the information provided in the context.

If the answer cannot be found in the context, reply:

"I couldn't find that information in the provided documents."

Answer in simple, clear English.

Context:
{context}

Question:
{question}

Answer:
""")

def ask_question(question):
    # Retrieve relevant documents
    docs = retriever.invoke(question)

    # Combine retrieved chunks into one context
    context = "\n\n".join(doc.page_content for doc in docs)

    # Create the prompt
    messages = prompt.invoke({
        "context": context,
        "question": question
    })

    # Ask the LLM
    response = llm.invoke(messages)

    # Extract source pages
    pages = sorted(set(doc.metadata.get("page_label", "?") for doc in docs))

    return response.content, pages