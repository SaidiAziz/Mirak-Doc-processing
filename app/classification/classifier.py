from transformers import pipeline

# TODO: Load your preferred model and tokenizer from Hugging Face
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

def classify_document(text, candidate_labels):
    """Classify document text into one of the candidate labels."""
    result = classifier(text, candidate_labels)
    return result['labels'][0] if result['labels'] else None

