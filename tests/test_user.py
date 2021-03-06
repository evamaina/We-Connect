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
from models.users import User


class UserAuthClass(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_user_can_register(self):
        """
        Test new user can be registered to the system.
        """
        response = self.app.post("/api/auth/register",
                                 data=json.dumps(dict(username="testusername2",
                                                      email="testEmail@gmail2.com",
                                                      password="testpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User created", response_msg["Message"])

    def test_user_email_validity(self):
        """
        Test new user uses a valid email.
        """
        response = self.app.post("/api/auth/register",
                                 data=json.dumps(dict(username="testusername",
                                                      email="testEmail",
                                                      password="testpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Please enter correct emaill and try again",
                      response_msg["Message"])

    def test_user_cannot_enter_blank(self):
        """
        Test new user can be registered to the system.
        """
        response = self.app.post("/api/auth/register",
                                 data=json.dumps(dict(username="",
                                                      email="testEmail@gmail.com",
                                                      password="testpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("You must enter username, Cannot be blank",
                         response_msg["Message"])

    def test_user_cannot_enter_whitespace(self):
        """
        Test new user can be registered to the system.
        """
        response = self.app.post("/api/auth/register",
                                 data=json.dumps(dict(username="  ",
                                                      email="testEmail@gmail.com",
                                                      password="testpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("You must enter username, Cannot be blank",
                         response_msg["Message"])

    def test_user_exists(self):
        """
        Test new user can be registered to the system.
        """
        response = self.app.post("/api/auth/register",
                                 data=json.dumps(dict(username="testusername",
                                                      email="testEmail@gmail.com",
                                                      password="testpassword")),
                                 content_type="application/json")
        response = self.app.post("/api/auth/register",
                                 data=json.dumps(dict(username="testusername",
                                                      email="testEmail@gmail.com",
                                                      password="testpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 409)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("User already exist", response_msg["Message"])

    def test_user_can_login(self):
        """
        Test new user can login to the system.
        """
        self.app.post("/api/auth/register",
                      data=json.dumps(dict(username="testusername1",
                                           email="testEmail1@gmail.com",
                                           password="testpassword")),
                      content_type="application/json")
        response = self.app.post("/api/auth/login",
                                 data=json.dumps(dict(
                                     username_or_email="testEmail1@gmail.com",
                                     password="testpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("logged in Successfuly", response_msg["Message"])

    def test_user_can_logout(self):
        """
        Test new user can login to the system.
        """
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

        response = self.app.post("/api/auth/logout",
                                 data=json.dumps(dict(
                                     username_or_email="testEmail@gmail.com",
                                     password="testpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("User logged out successfully", response_msg["Message"])

    def test_user_already_logged_in(self):
        """
        Test user already logged in to the system.
        """
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

        response = self.app.post("/api/auth/login",
                                 data=json.dumps(dict(
                                 username_or_email="testEmail@gmail.com",
                                 password="testpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 409)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("is already logged in", response_msg["Message"])

    def test_user_cannot_login_with_wrong_password(self):
        """
        Test new user can login to the system.
        """
        response = self.app.post("/api/auth/login",
                                 data=json.dumps(dict(
                                     username_or_email="testEmail@gmail.com",
                                     password="testpasswo")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("wrong username/password", response_msg["Message"])

    def test_user_cannot_login_with_wrong_username_or_email(self):
        """
        Test new user can login to the system.
        """
        response = self.app.post("/api/auth/login",
                                 data=json.dumps(dict(
                                     username_or_email="testEma@gmail.com",
                                     password="testpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("wrong username", response_msg["Message"])

    def test_user_not_logged_in(self):
        """
        Test new user can login to the system.
        """
        response = self.app.post("/api/auth/logout",
                                 data=json.dumps(dict(
                                     username_or_email="testEmail")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("User is not logged in", response_msg["Message"])

    def test_user_can_reset_password(self):
        """
        Tests new user can add a business to the system.
        """
        self.app.post("/api/auth/register",
                      data=json.dumps(dict(username="testusername",
                                           email="testEmail@gmail.com",
                                           password="testpassword")),
                      content_type="application/json")

        response = self.app.post("/api/auth/reset-password",
                                 data=json.dumps(dict(username="testusername",
                                                      old_password="testpassword",
                                                      new_password="testnewpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("password-reset done Successifuly",
                      response_msg["Message"])

    def test_user_cannot_reset_password_with_wrong_old_password(self):
        """
        Tests new user can add a business to the system.
        """
        self.app.post("/api/auth/register",
                      data=json.dumps(dict(username="testusername",
                                           email="testEmail@gmail.com",
                                           password="testpassword")),
                      content_type="application/json")

        response = self.app.post("/api/auth/reset-password",
                                 data=json.dumps(dict(username="testusername",
                                                      old_password="testpasswo",
                                                      new_password="testnewpassword")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Enter the new password and try again",
                      response_msg["Message"])

    def test_user_can_get_all_users(self):
        """
        Test user can get all users.
        """
        response = self.app.get("/api/auth/users",
                                data=json.dumps(dict()),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))

    #def tearDown(self):

