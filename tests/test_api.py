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
    def setUp(self):
        self.app = app.test_client()

    def test_user_can_register(self):
        """
        Test new user can be registered to the system.
        """
        response = self.app.post("/api/auth/register",
                                    data=json.dumps(dict(username="testusername",
                                                    password="testpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("registered", response_msg["Message"])

    def test_user_can_login(self):
        """
        Test new user can login to the system.
        """
        response = self.app.post("/api/auth/login",
                                    data=json.dumps(dict(username="testusername",
                                                    password="testpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("wrong username", response_msg["Message"])

    def test_user_can_register_business(self):
        """
        Tests new user can add a business to the system.
        """
        response = self.app.post("/api/business",
                                    data=json.dumps(dict(business_name="testbusinessname",
                                                    country="testcountry")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("registered successfully", response_msg["Message"])

    def test_user_can_update_business(self):
        """
        Tests new user can add a business to the system.
        """
        response = self.app.put("/api/businesses/<businessId>",
                                    data=json.dumps(dict(businessId="testbusinessid",
                                                    country="testcountry")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Business does not exist", response_msg["Message"])

    def test_user_can_reset_password(self):
        """
        Tests new user can add a business to the system.
        """
        response = self.app.post("/api/auth/reset-password",
                                    data=json.dumps(dict(username="testusername",
                                                    old_password="testpassword",
                                                    new_password="testnew")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("password-reset done Successifuly", response_msg["Message"])


    




    


