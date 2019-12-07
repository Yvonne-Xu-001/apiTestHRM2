import logging
import unittest
import requests

from api.login_api import LoginApi
from script.test_ihrm_employee_add import user_id, headers


class TestIHRMEmployeeCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_1_add_employee(self):
        response = requests.get(url="http://182.92.81.159/api/sys/user/{}".format(user_id),headers=headers)
        print(response.json())

