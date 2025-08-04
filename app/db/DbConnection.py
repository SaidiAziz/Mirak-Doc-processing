import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


class DbConnection:
    def __init__(self):
        required_env_vars = ["HOST", "DATABASE", "USER", "PASSWORD", "PORT"]
        missing_vars = [var for var in required_env_vars if not os.getenv(var)]
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

        self.host = os.getenv("HOST")
        self.database = os.getenv("DATABASE")
        self.user = os.getenv("USER")
    def create_engine(self):
        """Create and return SQLAlchemy engine."""
        try:
            db_url = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
            self.engine = create_engine(db_url)
            print(f"Engine created for database: {self.database}")
            return self.engine
        except Exception as e:
            print(f"Failed to create database engine: {e}")
            raise        """Create and return SQLAlchemy engine."""
        db_url = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        self.engine = create_engine(db_url)
        return self.engine

    def connect(self):
        """Establish a connection to the database."""
        if not self.engine:
            self.create_engine()
        try:
            self.connection = self.engine.connect()
            print("Database connection established successfully.")
            self.connection.close()  # Close the connection immediately if not needed
            return True
        except Exception as e:
            print(f"Failed to connect to the database: {e}")
            return False

    def get_engine(self):
        """Get the SQLAlchemy engine."""
#     except Exception as e:
#         print(f"Failed to connect to the database: {e}")
#
#     return engine
