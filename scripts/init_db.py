import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.Models import Base
from app.db.DbConnection import engine

if __name__ == "__main__":
    print("Creating database tables...")
    engine = engine()
    Base.metadata.create_all(bind=engine)
    print("Done.")


