from app.db.db_connection import connect_db


class DatabaseManager:
    def __init__(self):
        self.conn = connect_db()

    def execute_query(self, query, params=None, fetch=False):
        """Execute SQL query with error handling"""
        if not self.conn:
            print("No database connection")
            return False

        try:
            with self.conn.cursor() as cur:
                cur.execute(query, params)
                if fetch:
                    return cur.fetchall()
                self.conn.commit()
            return True
        except Exception as e:
            print(f"Query execution failed: {e}")
            self.conn.rollback()
            return False

    def close(self):
        """Close the database connection"""
        if self.conn:
            self.conn.close()
            print("Database connection closed")