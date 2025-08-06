import os
from app.ingestion.TextExtractor import TextExtractor
from app.tokenization.Tokenizer import Tokenizer
from app.db.DB_Manager import DBManager
from app.db.Models import Document, Token


def main():
    # Initialize components
    extractor = TextExtractor()
    tokenizer = Tokenizer()
    db_manager = DBManager()

    # File path input
    file_path = input("Enter the file path to extract text: ")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        # Step 1: Extract text
        extracted_text = extractor.extract(file_path)
        print(f"Text extracted from {file_path} successfully.")

        # Step 2: Tokenize text
        tokens = tokenizer.tokenize_text(extracted_text)
        phonetic_tokens = tokenizer.phonetic_tokenization(extracted_text)
        print("Tokens and phonetic tokens generated successfully.")

        # Step 3: Add data to the database
        with db_manager.session_manager.get_session() as session:
            # Add document
            document = Document(
                filename=os.path.basename(file_path),
                file_path=file_path,
                raw_text=extracted_text
            )
            document = db_manager.add_document(session, document)

            # Add tokens
            for position, (token, phonetic) in enumerate(zip(tokens, phonetic_tokens)):
                token_obj = Token(
                    document_id=document.id,
                    token=token,
                    phonetic_token=phonetic,
                    position=position
                )
                db_manager.add_token(session, token_obj)

            # Commit all changes
            session.commit()
            print(f"Data successfully added to the database for document ID {document.id}.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
