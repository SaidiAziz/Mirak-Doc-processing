import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()


class Classifier:
    """
        Classifier class to handle document classification using Hugging Face API.
        """

    def __init__(self, api_token_env="HUGGING_FACE_API_TOKEN", model_url=None, labels_file=None):
        """
        Initialize the Classifier with API token, model URL, and labels file path.
        """
        self.api_token = os.getenv(api_token_env)
        if not self.api_token:
            raise ValueError(f"{api_token_env} environment variable is required")

        self.api_url = model_url or "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}

        self.labels = self._load_labels(labels_file) if labels_file else []

    def _load_labels(self, labels_file):
        """
            Load classification labels from a JSON file.
            """
        with open(labels_file, 'r') as f:
            return list(json.load(f).keys())

    def classify_document(self, text, labels=None):
        """
            Send text to Hugging Face API for zero-shot classification.
            """
        if not text or not (labels or self.labels):
            raise ValueError("Both text and labels are required")

        payload = {"inputs": text, "parameters": {"candidate_labels": labels or self.labels}}
        response = requests.post(self.api_url, headers=self.headers, json=payload)

        if response.status_code != 200:
            raise RuntimeError(f"Hugging Face API error {response.status_code}: {response.text}")

        return response.json()
