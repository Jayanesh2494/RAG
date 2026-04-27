from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.retriever import get_retriever
from src.llm import load_llm


def build_rag():
    retriever = get_retriever()
    llm = load_llm()

    # Prompt template
    prompt = ChatPromptTemplate.from_template("""
    Answer the question based only on the context below.

    Context:
    {context}

    Question:
    {question}
    """)

    # Format retrieved docs
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # RAG chain (LCEL style)
    rag_chain = (
        {"context": retriever | format_docs, "question": lambda x: x}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain