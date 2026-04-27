from langchain_community.vectorstores import FAISS
from src.embeddings import get_embedding_model
from config import FAISS_PATH

embedding_model = get_embedding_model()

def create_vectorstore(chunks):
    db = FAISS.from_documents(chunks, embedding_model)
    db.save_local(FAISS_PATH)
    return db

def load_vectorstore():
    return FAISS.load_local(
        FAISS_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )