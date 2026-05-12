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
```
```

## System Architecture
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
## System Architecture
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
Installation
Clone Repository
git clone <your_repository_link>
cd agentic-rag
Install Dependencies
pip install -r requirements.txt
Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_api_key
LLM_MODEL=gpt-4o-mini
CHROMA_DIR=./chroma_db
COLLECTION_NAME=agentic_rag
TOP_K=5
SIMILARITY_THRESHOLD=0.30
Running the Project
Step 1 — Upload Documents

Add PDF, TXT, and CSV files into the project directory or upload them in Google Colab.

Example documents:
Research papers
SOP documents
Product datasets
FAQ documents
Step 2 — Run Application
python app.py
Example Queries
PDF-Based Questions
What is self-attention?
Explain transformers
What are multimodal transformers?
TXT-Based Questions
How many leave days are allowed?
Is remote work permitted?
CSV-Based Questions
What is the price of laptop?
Which products belong to Electronics category?
Hallucination Prevention

The system is specifically designed to reduce hallucinations.

The chatbot answers ONLY from retrieved document context.

If relevant information is unavailable, the system responds with:

I don't have enough information in the provided documents.
Sample Output
Question:
What is self-attention?

Answer:
Self-attention is a mechanism used in transformers that allows the model to focus on relevant parts of the input sequence while processing information.

Sources:
- attention_is_all_you_need.pdf
Challenges Faced
Efficient PDF text extraction
Managing chunk overlap
Reducing duplicate embeddings
Preventing hallucinated responses
Optimizing retrieval quality
Limitations
Large PDFs increase processing time
Retrieval quality depends on chunking strategy
Requires internet access for OpenAI API
Basic CLI interface only
Future Improvements
Streamlit web interface
Conversation memory
Multi-user support
Hybrid search (keyword + semantic)
Re-ranking models
Google Drive integration
Agent tool usage
Conclusion

This project demonstrates a complete end-to-end Retrieval-Augmented Generation (RAG) pipeline capable of handling multiple document formats and generating context-aware responses using modern AI technologies.

The system emphasizes modularity, scalability, and hallucination prevention while maintaining clean architecture and practical implementation.

Author

Mahani
BTech Student — IIT Hyderabad
