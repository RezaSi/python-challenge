import os
import sys
import unittest
import asyncio

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now you can import the BankAccount class from solution.py
from solution import async_file_download

class TestAsyncFileDownload(unittest.TestCase):
    def setUp(self):
        self.file_url = "https://example.com/file.txt"
        self.file_path = "test_file.txt"

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_async_file_download(self):
        loop = asyncio.get_event_loop()
        download_time = loop.run_until_complete(async_file_download(self.file_url, self.file_path))
        self.assertGreater(download_time, 0)
        self.assertTrue(os.path.exists(self.file_path))

if __name__ == '__main__':
    unittest.main()
