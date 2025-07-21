import unittest
from app.ingestion import file_loader

class TestFileLoader(unittest.TestCase):
    def test_load_file(self):
        self.assertIsNone(file_loader.load_file('dummy.txt'))

if __name__ == '__main__':
    unittest.main()


