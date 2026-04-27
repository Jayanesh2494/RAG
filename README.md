# 🚀 RAG-Based Document Question Answering System

A **Retrieval-Augmented Generation (RAG)** system that enables users to query information from documents (PDF/DOCX) using a **local LLM (LLaMA 3 via Ollama)**.
This project combines semantic search with generative AI to deliver **accurate, context-aware answers**.

---

## 📌 Overview

This system processes unstructured documents and allows users to ask natural language questions. It retrieves relevant context using vector similarity and generates responses using a large language model.

---

## 🧠 Architecture

```
Documents (PDF/DOCX)
        ↓
Text Cleaning & Chunking
        ↓
Embeddings (Sentence Transformers)
        ↓
Vector Store (FAISS)
        ↓
Retriever (Top-K Similar Chunks)
        ↓
LLM (LLaMA 3 via Ollama)
        ↓
Generated Answer
```

---

## ⚙️ Tech Stack

* **LLM**: LLaMA 3 (via Ollama)
* **Embeddings**: Sentence Transformers (HuggingFace)
* **Vector Database**: FAISS
* **Framework**: LangChain (latest modular architecture)
* **Languages**: Python

---

## 📁 Project Structure

```
rag-project/
│
├── data/                      # Input documents
├── vectorstore/              # FAISS index storage
├── src/
│   ├── loader.py             # Load PDF & DOCX
│   ├── splitter.py           # Chunking logic
│   ├── embeddings.py         # Embedding model
│   ├── vectorstore.py        # FAISS operations
│   ├── retriever.py          # Retrieval logic
│   ├── llm.py                # LLaMA (Ollama)
│   ├── rag_chain.py          # RAG pipeline
│
├── app.py                    # Entry point
├── config.py                 # Configurations
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone 
cd rag-project
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Setup LLM (Ollama)

Install Ollama and pull the model:

```bash
ollama pull llama3
```

Run the model:

```bash
ollama run llama3
```

---

## 📂 Add Your Documents

Place your files inside:

```
data/
 ├── sample.pdf
 ├── sample.docx
```

---

## ▶️ Run the Application

```bash
python app.py
```

---

## 💬 Example Usage

```
Ask: What is this document about?
Answer: ...
```

Type `exit` to quit.

---

## 🔥 Key Features

* 📄 Multi-format document support (PDF, DOCX)
* ✂️ Intelligent text chunking
* 🔍 Semantic search using FAISS
* 🧠 Context-aware answer generation
* 🖥️ Fully local LLM (privacy-friendly)
* ⚡ Modular and scalable architecture

---

## 🧠 How It Works

1. Documents are loaded and split into chunks
2. Each chunk is converted into embeddings
3. Embeddings are stored in FAISS
4. User query is converted into embedding
5. Top-K relevant chunks are retrieved
6. Context + query is passed to LLaMA
7. Final answer is generated

---


## 🧠 Interview Explanation

> Built a RAG pipeline that processes documents into embeddings stored in FAISS, retrieves relevant context using semantic search, and generates responses using a locally hosted LLaMA model via Ollama.

---

## 📌 Requirements

* Python 3.9+
* Ollama installed
* Minimum 8GB RAM (recommended)

---

## 🙌 Acknowledgements

* LangChain ecosystem
* HuggingFace Transformers
* FAISS (Facebook AI)
* Ollama

---

## ⭐ If you found this useful, give it a star!
