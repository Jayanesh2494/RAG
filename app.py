from src.loader import load_documents
from src.splitter import split_docs
from src.vectorstore import create_vectorstore
from src.rag_chain import build_rag

def setup():
    docs = load_documents()
    chunks = split_docs(docs)
    create_vectorstore(chunks)

def main():
    qa = build_rag()

    while True:
        query = input("Ask: ")
        if query.lower() == "exit":
            break
        print(qa.invoke(query))

if __name__ == "__main__":
    setup()
    main()