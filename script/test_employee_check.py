import logging
import unittest
import requests

from api.employee_api import EmployeeApi
from api.login_api import LoginApi


class TestIHRMEmployeeCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.employee_api = EmployeeApi()
        cls.session = requests.Session()
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_1_employee(self):
        response = self.employee_api.login(self.session,'13800000002','123456')
        logging.info("登录接口返回数据为{}".format(response.json()))

        response = self.employee_api.check(self.session)
        print(response.json())





