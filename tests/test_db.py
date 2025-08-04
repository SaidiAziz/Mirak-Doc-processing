import unittest
from unittest.mock import patch, MagicMock
from app.db.DB_Connection import DbConnection


class TestDbConnection(unittest.TestCase):

    @patch.dict('os.environ', {}, clear=True)
    def test_missing_env_vars(self):
        """Test that ValueError is raised when environment variables are missing."""
        with self.assertRaises(ValueError) as context:
            DbConnection()
        self.assertIn("Missing required environment variables", str(context.exception))

    @patch.dict('os.environ', {
        "HOST": "localhost",
        "DATABASE": "test_db",
        "USER": "test_user",
        "PASSWORD": "test_password",
        "PORT": "5432"
    })
    @patch('app.db.DbConnection.create_engine')
    def test_create_engine(self, mock_create_engine):
        """Test that the engine is created successfully."""
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        db_conn = DbConnection()
        engine = db_conn.create_engine()

        self.assertIsNotNone(engine)
        mock_create_engine.assert_called_once()

    @patch.dict('os.environ', {
        "HOST": "localhost",
        "DATABASE": "test_db",
        "USER": "test_user",
        "PASSWORD": "test_password",
        "PORT": "5432"
    })
    @patch('sqlalchemy.create_engine')
    def test_connect_success(self, mock_create_engine):
        """Test successful database connection."""
        mock_engine = MagicMock()
        mock_connection = MagicMock()
        mock_engine.connect.return_value = mock_connection
        mock_create_engine.return_value = mock_engine

        db_conn = DbConnection()
        result = db_conn.connect()

        self.assertTrue(result)
        mock_engine.connect.assert_called_once()
        mock_connection.close.assert_called_once()

    @patch.dict('os.environ', {
        "HOST": "localhost",
        "DATABASE": "test_db",
        "USER": "test_user",
        "PASSWORD": "test_password",
        "PORT": "5432"
    })
    @patch('sqlalchemy.create_engine')
    def test_connect_failure(self, mock_create_engine):
        """Test failed database connection."""
        mock_engine = MagicMock()
        mock_engine.connect.side_effect = Exception("Connection failed")
        mock_create_engine.return_value = mock_engine

        db_conn = DbConnection()
        result = db_conn.connect()

        self.assertFalse(result)
        mock_engine.connect.assert_called_once()


if __name__ == "__main__":
    unittest.main()