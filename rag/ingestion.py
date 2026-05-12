%%writefile rag/ingestion.py

import os
import csv
import hashlib
from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()

CHROMA_DIR = os.getenv("CHROMA_DIR", "./chroma_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "agentic_rag")

client = chromadb.PersistentClient(path=CHROMA_DIR)

embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_function
)


def read_pdf(path):
    text = ""
    reader = PdfReader(path)

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text


def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def read_csv(path):
    rows = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            rows.append(
                " | ".join(f"{k}: {v}" for k, v in row.items())
            )

    return "\n".join(rows)


def read_file(path):
    ext = Path(path).suffix.lower()

    if ext == ".pdf":
        return read_pdf(path)

    elif ext == ".txt":
        return read_txt(path)

    elif ext == ".csv":
        return read_csv(path)

    else:
        raise ValueError(f"Unsupported file: {ext}")


def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks


def generate_id(text):
    return hashlib.md5(text.encode()).hexdigest()


def ingest_documents():
    total = 0

    for file in os.listdir():
        if file.endswith((".pdf", ".txt", ".csv")):

            print(f"Processing: {file}")

            text = read_file(file)

            if not text.strip():
                continue

            chunks = chunk_text(text)

            for idx, chunk in enumerate(chunks):

                doc_id = generate_id(file + str(idx) + chunk[:50])

                collection.add(
                    ids=[doc_id],
                    documents=[chunk],
                    metadatas=[
                        {
                            "source": file,
                            "chunk_index": idx
                        }
                    ]
                )

                total += 1

    print(f"Total chunks stored: {total}")
