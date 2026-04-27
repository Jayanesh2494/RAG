from src.vectorstore import load_vectorstore
from config import TOP_K

def get_retriever(search_type="similarity"):
    """
    Returns a retriever with configurable search type.

    search_type options:
    - "similarity" (default)
    - "mmr" (diversity-based retrieval)
    """

    db = load_vectorstore()

    if search_type == "mmr":
        retriever = db.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": TOP_K,
                "fetch_k": 10  # fetch more, then diversify
            }
        )
    else:
        retriever = db.as_retriever(
            search_kwargs={"k": TOP_K}
        )

    return retriever