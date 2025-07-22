import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def connect_db():
    connection = psycopg2.connect(
        host=os.getenv("HOST"),  # Default to localhost if not set
        database=os.getenv("DATABASE"),  # Default to 'postgres' if not set
        user=os.getenv("USER"),  # Default to 'postgres' if not set
        password=os.getenv("PASSWORD"),  # Default to 'postgres' if not set
        port=os.getenv("PORT")  # Default PostgreSQL port
    )
    return connection


# At the bottom of services/connectDB.py
if __name__ == "__main__":
    try:
        conn = connect_db()  # or whatever your function is called
        print("Connection successful!")
        conn.close()
    except Exception as e:
        print(f"Connection failed: {e}")
