from langchain_text_splitters import RecursiveCharacterTextSplitter


def clean_text(text):
    """
    Clean extracted document text.
    """

    # Remove unnecessary spaces
    text = text.replace("\n\n", "\n")

    # Remove leading/trailing spaces
    text = text.strip()

    return text


def split_text(text):
    """
    Split document text into smaller chunks.
    """

    text = clean_text(text)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    return chunks