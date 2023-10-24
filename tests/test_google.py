import os
import unittest
from dotenv import load_dotenv
from python_api_example import py_srb_google_utils

class TestDotenv(unittest.TestCase):
    load_dotenv()
    port = os.getenv("PORT")
    google_handle = py_srb_google_utils.HandlgeGoogle()

    def test_google_service(self):
        expected = True

        input_values = (
            ('8', '80', 'h'),
        )

        actual = self.google_handle.read_google_sheet()

        print(actual)

        self.assertEqual(actual,expected)


if __name__ == "__main__":
    unittest.main()
