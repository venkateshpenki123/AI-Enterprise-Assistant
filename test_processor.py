from document_processor import split_text


text = """
Artificial Intelligence is a technology that allows computers
to perform tasks that normally require human intelligence.

Machine Learning is a subset of Artificial Intelligence.
It allows computers to learn patterns from data.

Generative AI can create text, images, code and other content.
"""


chunks = split_text(text)


print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):

    print("\n----------------------")

    print("Chunk", i + 1)

    print("----------------------")

    print(chunk)