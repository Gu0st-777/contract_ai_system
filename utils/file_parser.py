
import pdfplumber
from docx import Document

def parse_file(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join([p.extract_text() or "" for p in pdf.pages])
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
