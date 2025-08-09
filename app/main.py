import os
from app.ingestion.TextExtractor import TextExtractor
from app.tokenization.Tokenizer import Tokenizer
from app.db.DB_Manager import DBManager
from app.classification.Classifier import Classifier
from app.db.Models import Document, Token


def main():
    file_path = input("Enter the file path: ").strip()
    if not os.path.exists(file_path):
        print(f"[ERROR] File not found: {file_path}")
        return

    print("[INFO] Initializing components...")
    extractor = TextExtractor()
    tokenizer = Tokenizer()
    classifier = Classifier(labels_file="doc_types.json")
    db_manager = DBManager()

    try:
        # Step 1: Extract text
        print("[INFO] Extracting text from the file...")
        text = extractor.extract(file_path)
        print("[SUCCESS] Text extraction completed.")

        # Step 2: Tokenize text
        print("[INFO] Tokenizing the extracted text...")
        tokens = tokenizer.tokenize_text(text)
        phonetics = tokenizer.phonetic_tokenization(text)
        print("[SUCCESS] Tokenization completed.")

        # Step 3: Classify document
        print("[INFO] Classifying the document...")
        classification_result = classifier.classify_document(text)
        print("[SUCCESS] Classification completed. Here are the results:")
        for label, score in zip(classification_result['labels'], classification_result['scores']):
            print(f"  - Label: {label}, Confidence: {score:.2f}")
        selected_type = classification_result['labels'][0]
        print(f"[INFO] Selected Document Type: {selected_type}")

        # Confirm before adding data to the database
        proceed = input("Proceed with adding data to the database? (type 'yes' to continue): ").strip().lower()
        if proceed != 'yes':
            print("[INFO] Data addition to the database aborted by user.")
            return

        # Step 4: Add data to the database
        print("[INFO] Adding data to the database...")
        with db_manager.session_manager.get_session() as session:
            # Add document
            document = Document(
                filename=os.path.basename(file_path),
                file_path=file_path,
                raw_text=text,
                document_type=selected_type,
                classification_confidence=max(classification_result['scores']),
                json_result=classification_result
            )
            document = db_manager.add_document(session, document)
            print(f"[SUCCESS] Document added to the database with ID: {document.id}")

            # Add tokens
            for pos, (tok, phon) in enumerate(zip(tokens, phonetics)):
                db_manager.add_token(session, Token(
                    document_id=document.id,
                    token=tok,
                    phonetic_token=phon,
                    position=pos
                ))
            print("[SUCCESS] Tokens added to the database.")

            session.commit()
            print("[SUCCESS] All data committed to the database.")

    except Exception as e:
        print("[ERROR] An error occurred during processing:")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()