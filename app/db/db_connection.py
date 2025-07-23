import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def connect_db():
    try:
        connection = psycopg2.connect(
            host=os.getenv("HOST"),  # Default to localhost if not set
            database=os.getenv("DATABASE"),  # Default to 'postgres' if not set
            user=os.getenv("USER"),  # Default to 'postgres' if not set
            password=os.getenv("PASSWORD"),  # Default to 'postgres' if not set
            port=os.getenv("PORT")  # Default PostgreSQL port
        )
        print("Database connection successful")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None