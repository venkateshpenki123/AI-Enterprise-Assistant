import os
import fitz

from dotenv import load_dotenv
from google import genai


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()


# ==========================================
# GET GEMINI API KEY
# ==========================================

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )


# ==========================================
# CREATE GEMINI CLIENT
# ==========================================

client = genai.Client(
    api_key=api_key
)


# ==========================================
# OCR FUNCTION
# ==========================================

def extract_text_from_scanned_pdf(pdf_path):

    # Open PDF
    pdf = fitz.open(pdf_path)

    complete_text = ""


    # ======================================
    # PROCESS EACH PAGE
    # ======================================

    for page_number, page in enumerate(pdf):

        print(
            f"Processing page {page_number + 1}..."
        )


        # Convert page to image
        pix = page.get_pixmap(
            dpi=150
        )

        image_bytes = pix.tobytes(
            "png"
        )


        # ==================================
        # OCR PROMPT
        # ==================================

        prompt = """
Extract all readable text from this scanned
document page.

Rules:

1. Extract the text accurately.
2. Preserve the original meaning.
3. Do not summarize.
4. Do not explain anything.
5. Return only the extracted text.
"""


        # ==================================
        # SEND IMAGE TO GEMINI
        # ==================================

        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=[
                prompt,

                {
                    "inline_data": {
                        "mime_type": "image/png",
                        "data": image_bytes
                    }
                }
            ]
        )


        # ==================================
        # SAVE PAGE TEXT
        # ==================================

        complete_text += (
            f"\n\n--- Page "
            f"{page_number + 1} ---\n\n"
        )


        if response.text:

            complete_text += response.text

        else:

            complete_text += (
                "[No text extracted]"
            )


    # Close PDF
    pdf.close()


    return complete_text