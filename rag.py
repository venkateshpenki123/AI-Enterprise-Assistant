import os
from dotenv import load_dotenv
from google import genai

from vector_store import search_documents


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)


def ask_question(question, chunks, index):

    # Find relevant document chunks
    relevant_chunks = search_documents(
        question,
        chunks,
        index,
        top_k=3
    )

    # Combine relevant chunks
    context = "\n\n".join(
        relevant_chunks
    )

    prompt = f"""
You are an enterprise document assistant.

Answer the question using ONLY the
information in the document context.

If the answer is not present in the
context, say:
"I could not find this information
in the uploaded documents."

Do not make up information.

DOCUMENT CONTEXT:
{context}

QUESTION:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text, relevant_chunks