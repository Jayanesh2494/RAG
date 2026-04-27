from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
def load_documents():
    docs = []
    docs.extend(PyPDFLoader("data/sample.pdf").load())
    docs.extend(PyPDFLoader("data/samples.pdf").load())
    return docs