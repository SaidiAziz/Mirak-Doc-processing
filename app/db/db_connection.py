import os

import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


def engine():
    host = os.getenv("HOST")  # Default to localhost if not set
    database = os.getenv("DATABASE")  # Default to 'postgres' if not set
    user = os.getenv("USER")  # Default to 'postgres' if not set
    password = os.getenv("PASSWORD")  # Default to 'postgres' if not set
    port = os.getenv("PORT")  # Default PostgreSQL port

    db_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(db_url)

    try:
        connection = engine.connect()
        print("Database connection established successfully.")
        connection.close()
    except Exception as e:
        print(f"Failed to connect to the database: {e}")

    return engine
