import requests
import json
import os
from dotenv import load_dotenv
from app.ingestion.extraction import extract_text_from_pdf
from app.ingestion.file_loader import load_file

load_dotenv()

# ✅ Hugging Face API Token
API_TOKEN = os.getenv("HUGGING_FACE_API_TOKEN")
if not API_TOKEN:
    raise ValueError("HUGGING_FACE_API_TOKEN environment variable is required")

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def classify_document(text, labels):
    """
    Send text to Hugging Face API for zero-shot classification.
    """
    if not text or not labels:
        raise ValueError("Both text and labels are required")

    payload = {"inputs": text, "parameters": {"candidate_labels": labels}}

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise RuntimeError(f"Hugging Face API error {response.status_code}: {response.text}")
    return response.json()


# ✅ Load JSON labels
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(script_dir))
labels_path = os.path.join(script_dir, 'doc_types.json')
input_path = os.path.join(project_root, 'documents', 'inputs', 'img_2.png')

with open(labels_path, 'r') as f:
    doc_labels = json.load(f)
labels = list(doc_labels.keys())

# ✅ Extract text from PDF (with fallback)
try:
    text_to_classify = load_file(input_path)
except FileNotFoundError:
    print(f"⚠ sample.pdf not found at {input_path}! Using fallback text.")
    text_to_classify = "This is an invoice for services rendered."

# ✅ Classify
result = classify_document(text_to_classify, labels)

# ✅ Print nicely
print(json.dumps(result, indent=2))
