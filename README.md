# Agentic RAG Chatbot System

## Overview

This project is an AI-powered Agentic RAG (Retrieval-Augmented Generation) chatbot system developed as part of an AI Internship assignment.

The system ingests documents from multiple formats such as PDF, TXT, and CSV files, processes and chunks the data, generates embeddings, stores them in a vector database, retrieves relevant context based on user queries, and generates grounded responses using an LLM.

The chatbot is designed to minimize hallucinations by answering strictly from the ingested documents.

---

# Features

- Multi-format document ingestion
  - PDF
  - TXT
  - CSV

- Text preprocessing and chunking

- Embedding generation using Sentence Transformers

- Vector database storage using ChromaDB

- Semantic document retrieval

- LLM-powered response generation

- Hallucination prevention

- Source-aware answers

- Modular and scalable architecture

---

# Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Vector Database | ChromaDB |
| Embedding Model | all-MiniLM-L6-v2 |
| LLM | OpenAI GPT-4o-mini |
| PDF Processing | PyPDF |
| Environment | Google Colab |
| Framework | Custom RAG Pipeline |

---

# Project Structure

```text
agentic-rag/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
│
├── rag/
│   ├── ingestion.py
│   ├── retrieval.py
│   ├── generator.py
│   └── agent.py
│
├── data/
│
└── chroma_db/
'''
---
# System Architecture
Documents
   ↓
Document Loader
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embedding Generation
   ↓
Chroma Vector Database
   ↓
Retriever
   ↓
LLM
   ↓
Generated Answer

