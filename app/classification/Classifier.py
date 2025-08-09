import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()


class Classifier:
    def __init__(self, api_token_env="HUGGING_FACE_API_TOKEN", model_url=None, labels_file=None):
        self.api_token = os.getenv(api_token_env)
        if not self.api_token:
            raise ValueError(f"{api_token_env} environment variable is required")

        self.api_url = model_url or "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}

        # Resolve labels_file to absolute path if provided
        self.labels = []
        if labels_file:
            # Convert to absolute path based on current script location
            abs_labels_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), labels_file)
            self.labels = self.load_labels(abs_labels_path)

    @staticmethod
    def load_labels(labels_file):
        """Load labels from JSON file with existence check."""
        if not os.path.exists(labels_file):
            raise FileNotFoundError(f"Labels file not found: {labels_file}")

        with open(labels_file, 'r') as f:
            return list(json.load(f).keys())

    def classify_document(self, text, labels=None):
        """Classify text using Hugging Face API."""
        labels = labels or self.labels  # Use class labels if none provided
        if not text or not labels:
            raise ValueError("Text and labels are required")

        payload = {
            "inputs": text,
            "parameters": {"candidate_labels": labels}
        }
        response = requests.post(self.api_url, headers=self.headers, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()