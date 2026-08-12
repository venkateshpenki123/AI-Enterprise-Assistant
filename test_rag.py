from rag import ask_question
from vector_store import create_vector_store


chunks = [
    "The company provides health insurance to all full-time employees.",

    "Employees receive 20 days of paid annual leave every year.",

    "The company working hours are 9 AM to 6 PM from Monday to Friday.",

    "Employees can work remotely two days per week with manager approval."
]


print("Creating vector store...")

index = create_vector_store(
    chunks
)

print("Vector store created successfully!")


question = input(
    "\nAsk a question: "
)


print("\nSearching documents...")


answer, sources = ask_question(
    question,
    chunks,
    index
)


print("\n====================")
print("AI ANSWER")
print("====================")

print(answer)


print("\n====================")
print("RETRIEVED SOURCES")
print("====================")

for i, source in enumerate(sources):

    print(f"\nSource {i + 1}:")
    print(source)