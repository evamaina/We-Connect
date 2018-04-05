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
from models.users import User
from models.business import Business


class TestReviewsClassFunctionality(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_review_to_business(self):
        """
        Ensuring user is registered before adding a review.
        """
        self.app.post("/api/auth/register",
                      data=json.dumps(dict(username="testusername",
                                           email="testEmail@gmail.com",
                                           password="testpassword")),
                      content_type="application/json")
        # ensuring user is logged in before adding review
        self.app.post("/api/auth/login",
                      data=json.dumps(dict(
                          username_or_email="testEmail@gmail.com",
                          password="testpassword")),
                      content_type="application/json")
        # business must for a review to be added
        self.app.post("/api/business",
                      data=json.dumps(dict(userid=1,
                                           business_name="testbusiness_name",
                                           country="test_country")),
                      content_type="application/json")
        # adding review to a business
        response = self.app.post("/api/businesses/1/reviews",
                                 data=json.dumps(dict(username="testusername",
                                                      businessid=1,
                                                      title="Discovery",
                                                      body="great")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("review created", response_msg["Message"])

    def test_add_review_without_user_account(self):
        """
        Tests new user cannnot add a review without user account
        """
        response = self.app.post("/api/businesses/1/reviews",
                                 data=json.dumps(dict(username="testusername",
                                                      title="title1",
                                                      body="review")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Use user account that exist in the system",
                      response_msg["Message"])

    def test_add_review_to_business_that_does_not_exist(self):

        self.app.post("/api/auth/register",
                      data=json.dumps(dict(username="testusername",
                                           email="testEmail@gmail.com",
                                           password="testpassword")),
                      content_type="application/json")
        self.app.post("/api/auth/login",
                      data=json.dumps(dict(
                          username_or_email="testEmail@gmail.com",
                          password="testpassword")),
                      content_type="application/json")
        self.app.post("/api/business",
                      data=json.dumps(dict(userid=1,
                                           business_name="testbusiness_name",
                                           country="test_country")),
                      content_type="application/json")
        """
        Tests user cannot add a review to a business that does not exist.
        """
        response = self.app.post("/api/businesses/10/reviews",
                                 data=json.dumps(dict(username="testusername",
                                                      title="good",
                                                      body="review")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("No business record found", response_msg["Message"])

    def test_user_can_retrieve_all_reviews(self):
        """
        Tests user can get all business reviews.
        """
        response = self.app.get("/api/businesses/reviews",
                                data=json.dumps(dict()),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)
        # response_msg = json.loads(response.data.decode("UTF-8"))
