%%writefile rag/retrieval.py

from rag.ingestion import collection


def retrieve(query, top_k=5):

    results = collection.query(
        query_texts=[query],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    chunks = []

    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):

        chunks.append(
            {
                "text": doc,
                "source": meta["source"],
                "score": 1 - dist
            }
        )

    chunks.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return chunks
