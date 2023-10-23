import os
import unittest
from dotenv import load_dotenv


class TestDotenv(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.env_variable = os.getenv("ENV")
        self.team_web_hook = os.getenv("TEAMS_PYTHON_WEB_HOOK")
        self.service_now_user = os.getenv("SERVICENOW_PROD_USER")

    def test_env_variables_exist(self):
        self.assertIsNotNone(self.team_web_hook)

    def test_env_variable_is_string(self):
        self.assertIsInstance(self.env_variable, str)

    def test_jira_server_variables_are_correct_strings(self):
        expected = "svc_qacoejira_p"
        actual = os.getenv("JIRA_PROD_USER")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
