import os
import unittest
from dotenv import load_dotenv


class TestDotenv(unittest.TestCase):
    load_dotenv()
    port = os.getenv("PORT")

    def test_port_exists(self):
        self.assertIsNotNone(self.port)


if __name__ == "__main__":
    unittest.main()
