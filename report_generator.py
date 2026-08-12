import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )

client = genai.Client(
    api_key=api_key
)


def generate_report(data):

    # Convert data to text
    if hasattr(data, "to_string"):

        data_text = data.to_string(
            index=False
        )

    else:

        data_text = str(data)

    prompt = f"""
You are an enterprise data analyst.

Analyze the following data:

{data_text}

Generate a concise report with:

1. Executive Summary
2. Key Findings
3. Important Insights
4. Recommendations
5. Conclusion

Use only the information present in the data.
Do not invent facts.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    if not response.text:

        return "No report was generated."

    return response.text