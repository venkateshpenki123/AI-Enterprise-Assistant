import os
from database import SessionLocal, Document

db = SessionLocal()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_document(uploaded_file):

    filepath = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    doc = Document(
        filename=uploaded_file.name,
        filetype=uploaded_file.type,
        filepath=filepath
    )

    db.add(doc)
    db.commit()

    return filepath


def get_documents():

    return db.query(Document).all()