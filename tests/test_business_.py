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
from models.business import Business
from models.users import User


class TestBusinessClassFunctionality(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_register_business(self):
        """
        Tests new user can add a business to the system.
        """
        response = self.app.post("/api/business",
                                 data=json.dumps(dict(userid=1,
                                 business_name="testbusiness_name",
                                 country="test_country")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Business created", response_msg["Message"])

    def test_register_business_exist(self):
        """
        Tests business already exists to the system.
        """
        response = self.app.post("/api/business",
                                 data=json.dumps(dict(business_name=
                                 "testbusiness_name",
                                 country="test_country", userid=1)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("business already exists", response_msg["Message"])



    def test_blank_business_name(self):
        """
        Tests a user can update his business to the system.
        """
        response = self.app.post("/api/businesses/1",
                                 data=json.dumps(dict(business_name=
                                 "",
                                 country="rwanda", userid=1)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Cannot be blank", response_msg["Message"])

    def test_user_cannot_use_whitespace(self):
        """
        Tests a user can update his business to the system.
        """
        response = self.app.post("/api/businesses/1",
                                 data=json.dumps(dict(business_name=
                                 "",
                                 country="rwanda", userid=1)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Cannot be blank", response_msg["Message"])

    def test_no_business_record_to_update(self):
        """
        Tests a user can update his business to the system.
        """
        response = self.app.post("/api/businesses/5",
                                 data=json.dumps(dict(business_name=
                                 "test",
                                 country="kenya", userid=1)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("no business record to update", response_msg["Message"])



    def test_update_business(self):
        """
        Tests a user can update his business to the system.
        """
        response = self.app.put("/api/businesses/1",
                                 data=json.dumps(dict(business_name=
                                 "testbusiness",
                                 country="rwanda", userid=1)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Business Updated", response_msg["Message"])



    def test_no_business_record_to_update(self):
        """
        Tests a user can update his business to the system.
        """
        response = self.app.put("/api/businesses/5",
                                 data=json.dumps(dict(business_name=
                                 "testbusiness",
                                 country="malawi", userid=5)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("no business record to update", response_msg["Message"])

    def test_user_can_get_business_by_id(self):
        """
        Tests a user can update his business to the system.
        """
        response = self.app.get("/api/businesses/1",
                                 data=json.dumps(dict(business_Id=1)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 302)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Business found", response_msg["Message"])

    def test_business_by_id_does_not_exist(self):
        """
        Tests a user can update his business to the system.
        """
        response = self.app.get("/api/businesses/10",
                                 data=json.dumps(dict(business_Id=10)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("No business record found", response_msg["Message"])

    def test_business_can_be_removed(self):
        """
        Tests a user can update his business to the system.
        """
        response = self.app.delete("/api/businesses/1",
                                 data=json.dumps(dict(business_Id=1)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Business Removed Successifuly", response_msg["Message"])

    def test_no_business_record_to_remove(self):
        """
        Tests a user can update his business to the system.
        """
        response = self.app.delete("/api/businesses/15",
                                 data=json.dumps(dict(business_Id=15)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("No business record to remove", response_msg["Message"])

    def test_user_can_retrieve_all_business(self):
        """
        Tests a user can get all business in the system.
        """
        response = self.app.get("/api/businesses",
                                 data=json.dumps(dict()),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("message", response_msg["Message"])
    
    
    










