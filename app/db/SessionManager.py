# session_manager.py
import contextlib

from sqlalchemy.orm import sessionmaker
from app.db.DB_Connection import DbConnection


class SessionManager:
    def __init__(self):
        db_connection = DbConnection()
        self.engine = db_connection.get_engine()
        self.SessionLocal = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)

    @contextlib.contextmanager
    def get_session(self):
        """
        Provides a new SQLAlchemy session.
        Ensures proper cleanup using a context manager.
        """
        session = self.SessionLocal()
        try:
            yield session
        finally:
            session.close()
