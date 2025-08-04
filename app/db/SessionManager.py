# session_manager.py
from sqlalchemy.orm import sessionmaker
from app.db.DbConnection import DbConnection


class SessionManager:
    def __init__(self):
        db_connection = DbConnection()
        self.engine = db_connection.get_engine()
        self.SessionLocal = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)

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
