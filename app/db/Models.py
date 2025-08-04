from sqlalchemy import (
    Column, Integer, String, Text, Float, ForeignKey, DateTime, JSON
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)
    file_path = Column(Text)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    raw_text = Column(Text)
    document_type = Column(String)  # e.g., "invoice", "passport"
    classification_confidence = Column(Float)
    json_result = Column(JSON)

    tokens = relationship("Token", back_populates="document", cascade="all, delete-orphan")
    embedding = relationship("DocumentEmbedding", uselist=False, back_populates="document")


class Token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey('documents.id', ondelete='CASCADE'))
    token = Column(String)
    phonetic_token = Column(String)
    position = Column(Integer)

    document = relationship("Document", back_populates="tokens")


class DocumentType(Base):
    __tablename__ = 'document_types'

    id = Column(Integer, primary_key=True)
    type_name = Column(String, unique=True)
    description = Column(Text)
    schema = Column(JSON)  # stores your custom structure or field hints


class DocumentEmbedding(Base):
    __tablename__ = 'document_embeddings'

    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey('documents.id', ondelete='CASCADE'))
    vector = Column(Text)  # Store as string if not using pgvector

    document = relationship("Document", back_populates="embedding")
