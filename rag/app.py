%%writefile app.py

from rag.ingestion import ingest_documents
from rag.agent import RAGAgent

print("Ingesting documents...")

ingest_documents()

print("Documents ingested successfully.")

agent = RAGAgent()

while True:

    query = input("\nAsk a question: ")

    if query.lower() in ["exit", "quit"]:
        break

    answer, sources = agent.ask(query)

    print("\nAnswer:")
    print(answer)

    print("\nSources:")

    for s in sources:
        print(
            f"- {s['source']} | score={s['score']:.2f}"
        )
