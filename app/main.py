import os
from app.config import load_config
from app.db.DB_Manager import add_document, add_token
from app.db.SessionManager import SessionManager
from app.db.Models import Document, Token
from app.ingestion.TextExtractor import extract_text_from_pdf
from app.ingestion.file_loader import load_file
from app.ingestion.ocr import extract_text_from_image
from app.tokenization.Tokenizer import tokenize_text, phonetic_tokenization


def main():
    config = load_config()
    print("Main application logic goes here.")

    # Initialize SessionManager
    session_manager = SessionManager()

    # Use a context manager to handle the session
    with session_manager.get_session() as session:
        try:
            # Get the project root directory (parent of the app directory)
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            input_path = os.path.join(project_root, "documents", "inputs", "img_1.jpg")
            text = extract_text_from_image(input_path)  # Example file path, replace with actual file input

            print(f"Extracted text:", text)  # Print first 100 characters for debugging

            # Tokenize extracted text
            tokenized_text = tokenize_text(text)
            print(f"Tokenized text:", tokenized_text)  # Print first 10 tokens for debugging

            phonetic_tokens = phonetic_tokenization(text)
            print(f"Phonetic tokens:", phonetic_tokens)  # Print first 10 phonetic tokens for debugging

            # Store tokens in the database
            document = Document(
                filename=os.path.basename(input_path),
                file_path=input_path,
                raw_text=text,
            )
            document = add_document(session, document)  # Pass existing session

            for position, (token, phonetic) in enumerate(zip(tokenized_text, phonetic_tokens)):
                token_obj = Token(
                    document_id=document.id,
                    token=token,
                    phonetic_token=phonetic,
                    position=position
                )
                add_token(session, token_obj)  # Pass existing session

            # Commit all operations at once
            session.commit()
            print(f"Stored {len(tokenized_text)} tokens in the database for document ID {document.id}.")

        except Exception as e:
            session.rollback()
            print(f"Database error: {str(e)}")
            raise


if __name__ == "__main__":
    main()