# services/pdf_parser.py

import pdfplumber
from typing import IO

def extract_text_from_pdf(file: IO) -> str:
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()
