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
from models.reviews import Reviews


class TestReviewsClassFunctionality(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_without_user_account(self):
        """
        Tests new user can add a business to the system.
        """
        response = self.app.post("/api/businesses/1/reviews",
                                    data=json.dumps(dict(username="testusername",
                                        title="title1", body="review")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Use user account that exist in the system", response_msg["Message"])

    
