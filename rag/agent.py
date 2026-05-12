%%writefile rag/agent.py

from rag.retrieval import retrieve
from rag.generator import generate_answer


class RAGAgent:

    def ask(self, query):

        chunks = retrieve(query)

        relevant = [
            c for c in chunks
            if c["score"] > 0.30
        ]

        if not relevant:
            return (
                "I don't have enough information in the provided documents.",
                []
            )

        answer = generate_answer(
            query,
            relevant
        )

        return answer, relevant
