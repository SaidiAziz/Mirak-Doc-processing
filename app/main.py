from app.config import load_config
from app.ingestion.extraction import extract_text_from_pdf
from app.ingestion.file_loader import load_file
from app.tokenization.phonetic_tokenizer import tokenize_text, phonetic_tokenization


def main():
    # config = load_config()
    # print("Document Processing System Started.")
    # print(f"Loaded config: {config}")

    print("Main application logic goes here.")

    input_path = "documents/inputs/sample.pdf"  # Example file path, replace with actual file input
    text = extract_text_from_pdf(input_path)  # Example file path, replace with actual file input

    print(f"Extracted text: {text[:100]}...")  # Print first 100 characters for debugging

    # TODO 5: tokenize extracted text

    tokenized_text = tokenize_text(text)  # Simple split for demonstration, replace with actual tokenizer
    print(f"Tokenized text: {tokenized_text[:10]}...")  # Print first 10 tokens for debugging

    phoentic_tokens = phonetic_tokenization(text)
    print(f"Phonetic tokens: {phoentic_tokens[:10]}...")  # Print first 10 phonetic tokens for debugging

    # TODO 6: store tokens in database
    # TODO 7: return tokens to user


if __name__ == "__main__":
    main()
