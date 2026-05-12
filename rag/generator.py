%%writefile rag/generator.py

import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")


def generate_answer(query, chunks):

    if not chunks:
        return "I don't have enough information in the provided documents."

    context = "\n\n".join(
        [
            f"[Source: {c['source']}]\n{c['text']}"
            for c in chunks
        ]
    )

    prompt = f"""
You are an AI document assistant.

Answer ONLY from the provided context.

If answer is not available in context, say:
'I don't have enough information in the provided documents.'

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.1,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
