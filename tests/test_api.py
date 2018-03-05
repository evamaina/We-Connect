import unittest
import json
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from src.api import app


class UserAuthClass(unittest.TestCase):
    def setup(self):
        self.app = app.test_client()
    """
    Test user registration and login.
    """
    def test_user_can_register(self):
        """Test new user can be added to the system."""
        response = self.app.post("/api/auth/register",
                                    data=json.dumps(dict(username="testusername",
                                                    password="testpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("registered", response_msg["Message"])

if __name__ == '__main__':
    unittest.main()