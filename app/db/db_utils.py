from sqlalchemy.orm import Session

from app.db.SessionManager import SessionManager
from app.db.models import Document, Token, DocumentType, DocumentEmbedding

session_manager = SessionManager.get_session()


def add_document(session: Session, document: Document):
    """
    Adds a new document to the database using an existing session.

    Args:
        session (Session): Existing SQLAlchemy session
        document (Document): The document instance to add.

    Returns:
        Document: The added document instance with its ID populated.
    """
    try:
        session.add(document)
        session.commit()
        session.refresh(document)  # Refresh to populate auto-generated fields
        return document
    except Exception as e:
        session.rollback()
        raise e


def add_token(session: Session, token: Token):
    """
    Adds a new token to the database using an existing session.

    Args:
        session (Session): Existing SQLAlchemy session
        token (Token): The token instance to add.

    Returns:
        Token: The added token instance with its ID populated.
    """
    try:
        session.add(token)
        return token
    except Exception as e:
        session.rollback()
        raise e


# Update other functions similarly (for document types and embeddings)
def add_document_type(session: Session, document_type: DocumentType):
    try:
        session.add(document_type)
        return document_type
    except Exception as e:
        session.rollback()
        raise e


def add_document_embedding(session: Session, document_embedding: DocumentEmbedding):
    try:
        session.add(document_embedding)
        return document_embedding
    except Exception as e:
        session.rollback()
        raise e
