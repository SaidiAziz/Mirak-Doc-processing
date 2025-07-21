import pymupdf


def extract_text_from_pdf(input_path):
    """
    Extract text from a PDF file using PyMuPDF.
    """
    doc = pymupdf.open(input_path)  # Open the PDF file
    text = ""

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load each page
        text += page.get_text()  # Extract text from the page
    return text
