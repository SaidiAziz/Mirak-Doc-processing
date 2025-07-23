from sqlalchemy.orm import sessionmaker

from app.db.db_connection import engine
from app.db.models import Document, Token, DocumentType, DocumentEmbedding


def get_session():
    """
    Creates a new SQLAlchemy session.

    Returns:
        Session: A new session instance.
    """
    Session = sessionmaker(bind=engine)
    return Session()


def add_document(document: Document):
    """
    Adds a new document to the database.

    Args:
        document (Document): The document instance to add.

    Returns:
        Document: The added document instance with its ID populated.
    """
    session = get_session()
    try:
        session.add(document)
        session.commit()
        return document
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def add_token(token: Token):
    """
    Adds a new token to the database.

    Args:
        token (Token): The token instance to add.

    Returns:
        Token: The added token instance with its ID populated.
    """
    session = get_session()
    try:
        session.add(token)
        session.commit()
        return token
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def add_document_type(document_type: DocumentType):
    """
    Adds a new document type to the database.

    Args:
        document_type (DocumentType): The document type instance to add.

    Returns:
        DocumentType: The added document type instance with its ID populated.
    """
    session = get_session()
    try:
        session.add(document_type)
        session.commit()
        return document_type
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def add_document_embedding(document_embedding: DocumentEmbedding):
    """
    Adds a new document embedding to the database.

    Args:
        document_embedding (DocumentEmbedding): The document embedding instance to add.

    Returns:
        DocumentEmbedding: The added document embedding instance with its ID populated.
    """
    session = get_session()
    try:
        session.add(document_embedding)
        session.commit()
        return document_embedding
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
