import requests
import json

from app.ingestion.extraction import extract_text_from_pdf

import os

from dotenv import load_dotenv

load_dotenv()

# ✅ Your Hugging Face API Token
API_TOKEN = os.getenv("HUGGING_FACE_API_TOKEN")
if not API_TOKEN:
    raise ValueError("HUGGING_FACE_API_TOKEN environment variable is required")
# ✅ Hugging Face Inference API endpoint
API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"

headers = {"Authorization": f"Bearer {API_TOKEN}"}


def classify_document(text, labels):
    """
    Classify text into one of the given labels using Hugging Face API.
    """
    if not text or not labels:
        raise ValueError("Both text and labels are required")

    payload = {
        "inputs": text,
        "parameters": {"candidate_labels": labels},
    }


# ✅ Example JSON with labels
try:
    with open('doc_types.json', 'r') as f:
        doc_labels = json.load(f)
except FileNotFoundError:
    raise FileNotFoundError("doc_types.json file not found")
except json.JSONDecodeError as e:
    raise ValueError(f"Invalid JSON in doc_types.json: {e}")

# ✅ Extract labels from JSON
labels = list(doc_labels.keys())
if not labels:
    raise ValueError("No labels found in doc_types.json")

# ✅ Simulated extracted text from PostgreSQL or OCR
try:
    text_to_classify = extract_text_from_pdf("documents/inputs/sample.pdf")
except Exception as e:
    raise RuntimeError(f"Failed to extract text from PDF: {e}")# ✅ Example JSON with labels
with open('doc_types.json', 'r') as f:
    doc_labels = json.load(f)

# ✅ Extract labels from JSON
labels = list(doc_labels.keys())

# ✅ Simulated extracted text from PostgreSQL or OCR
text_to_classify = extract_text_from_pdf("documents/inputs/sample.pdf")
# text_to_classify = "This is a sample document text that needs to be classified."

# ✅ Classify
result = classify_document(text_to_classify, labels)

print(json.dumps(result, indent=2))
