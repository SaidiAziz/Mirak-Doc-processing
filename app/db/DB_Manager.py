from app.db.SessionManager import SessionManager
from app.db.Models import Document, Token, DocumentType, DocumentEmbedding


class DBManager:
    def __init__(self):
        self.session_manager = SessionManager()

    def add_document(self, session, document: Document):
        try:
            session.add(document)
            session.flush()  # Flush to get the document ID
            session.refresh(document)
            return document
        except Exception as e:
            session.rollback()
            raise e

    def add_token(self, session, token: Token):
        try:
            session.add(token)
        except Exception as e:
            session.rollback()
            raise e
    def add_document_type(self, document_type: DocumentType):
        """
                Adds a new document type to the database.

                Args:
                    document_type (DocumentType): The document type instance to add.

                Returns:
                    DocumentType: The added document type instance.
                """
        with self.session_manager.get_session() as session:
            try:
                session.add(document_type)
                session.commit()
                session.refresh(document_type)
                return document_type
            except Exception as e:
                session.rollback()
                raise e

    def add_document_embedding(self, document_embedding: DocumentEmbedding):
        """
                Adds a new document embedding to the database.

                Args:
                    document_embedding (DocumentEmbedding): The document embedding instance to add.

                Returns:
                    DocumentEmbedding: The added document embedding instance.
                """
        with self.session_manager.get_session() as session:
            try:
                session.add(document_embedding)
                session.commit()
                session.refresh(document_embedding)
                return document_embedding
            except Exception as e:
                session.rollback()
                raise e
