import pymupdf
import pytesseract
from PIL import Image


class TextExtractor:

    def __init__(self):
        """
        Initialize the TextExtractor class.
        This class is responsible for extracting text from various file formats.
        """
        pass

    def extract(self, file_path):
        """
        Extract text from a file based on its type.
        Supports PDF and image files.

        :param file_path: Path to the file from which text is to be extracted.
        :return: Extracted text as a string.
        """
        ext = file_path.split('.')[-1].lower()
        if ext == 'pdf':
            return self.extract_text_from_pdf(file_path)

        # elif ext == '.docx':
        #   return extract_text_from_docx(file_path)
        # elif ext == '.txt':
        #   return extract_text_from_txt(file_path)

        elif ext in ['jpg', 'jpeg', 'png', 'bmp', 'gif']:
            return self.extract_text_from_image(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")

    @staticmethod
    def extract_text_from_pdf(file_path):
        """
        Extract text from a PDF file using PyMuPDF.
        """
        doc = pymupdf.open(file_path)  # Open the PDF file
        text = ""

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)  # Load each page
            text += page.get_text()  # Extract text from the page
        return text

    @staticmethod
    def extract_text_from_image(file_path):
        """Stub: Extract text from an image file using OCR."""
        if not pytesseract or not Image:
            raise ImportError("pytesseract and Pillow are required for OCR.")
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text
