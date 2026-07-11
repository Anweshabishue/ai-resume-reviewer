import io
import os
from pathlib import Path

import PyPDF2
from dotenv import load_dotenv

from groq import Groq

from config import MAX_RESUME_CHARS, MODEL, TEMPERATURE

load_dotenv()

_PROMPTS = Path(__file__).parent / "prompts"
REVIEW_PROMPT_TEXT = (_PROMPTS / "review.txt").read_text(encoding="utf-8")


def extract_text_from_pdf(uploaded_file) -> str:
    uploaded_file.seek(0)
    reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages).strip()


def review_resume(resume_text: str, job_role: str = "") -> str:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found.")

    client = Groq(api_key=api_key)

    job_context = (
        f"The candidate is targeting this role: {job_role}\n"
        if job_role else ""
    )

    prompt = REVIEW_PROMPT_TEXT.format(
        resume=resume_text[:MAX_RESUME_CHARS],
        job_context=job_context
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=TEMPERATURE
        
    )

    return response.choices[0].message.content