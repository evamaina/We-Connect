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
                                    data=json.dumps(dict(userid=1, business_name="testbusiness_name",
                                                    country="test_country")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Business created", response_msg["Message"])

    def test_register_business_exist(self):
        """
        Tests new user can add a business to the system.
        """
        response = self.app.post("/api/business",
                                    data=json.dumps(dict(business_name="testbusiness_name",
                                                    country="testcountry", userid=1)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("business already exists", response_msg["Message"])


    


