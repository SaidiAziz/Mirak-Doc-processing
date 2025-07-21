try:
    import pytesseract
    from PIL import Image
except ImportError:
    pytesseract = None
    Image = None


def extract_text_from_image(image_path):
    """Stub: Extract text from an image file using OCR."""
    if not pytesseract or not Image:
        raise ImportError("pytesseract and Pillow are required for OCR.")
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text
