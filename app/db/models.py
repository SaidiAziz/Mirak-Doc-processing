from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    filename = Column(Text, nullable=False)
    file_path = Column(Text)
    uploaded_at = Column(DateTime, server_default=func.now())
    raw_text = Column(Text)
    document_type = Column(Text)  # e.g., "invoice", "passport"
    classification_confidence = Column(Float)
    json_result = Column(JSON)  # Optional: full LLM result


class Token(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey('documents.id', ondelete='CASCADE'))
    token = Column(Text)
    phonetic_token = Column(Text)  # e.g., using Metaphone
    position = Column(Integer)  # Word position in text


class DocumentType(Base):
    __tablename__ = 'document_types'
    id = Column(Integer, primary_key=True)
    type_name = Column(Text, unique=True)
    description = Column(Text)
    schema = Column(JSON)  # Optional: structure/matching fields
