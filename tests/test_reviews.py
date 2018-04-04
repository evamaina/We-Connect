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

    def test_add_review_to_business(self):
        """
        Tests a user can add review to business.
        """
        response = self.app.post("/api/businesses/1/reviews",
                                 data=json.dumps(dict(username=
                                 "Evet",
                                 businessid=1, title="Discovery",
                                 body="great")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("review created", response_msg["Message"])

    def test_add_review_without_user_account(self):
        """
        Tests new user can add a business to the system.
        """
        response = self.app.post("/api/businesses/1/reviews",
                                 data=json.dumps(dict(username="testusername",
                                 title="title1", body="review")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Use user account that exist in the system",
                      response_msg["Message"])

    def test_add_review_to_business_that_does_not_exist(self):
        """
        Tests user cant add a review to a business that does not exist.
        """
        response = self.app.post("/api/businesses/10/reviews",
                                    data=json.dumps(dict(username="Evet",
                                        title="good", body="review")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("No business record found", response_msg["Message"])

    def test_user_can_retrieve_all_reviews(self):
        """
        Tests user can get all business reviews.
        """
        response = self.app.get("/api/businesses/reviews",
                                    data=json.dumps(dict(username="testusername",
                                        title="title1", body="review")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("review", response_msg["Message"])




