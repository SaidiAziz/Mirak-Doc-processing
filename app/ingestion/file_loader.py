import os

from app.ingestion.extraction import extract_text_from_pdf
from app.ingestion.ocr import extract_text_from_image


def load_file(file_path):
    """Stub: Load a file and return its content as text or image."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    # elif ext == '.docx':
    #   return extract_text_from_docx(file_path)
    # elif ext == '.txt':
    #   return extract_text_from_txt(file_path)
    else:
        # For images, delegate to OCR
        return extract_text_from_image(file_path)
