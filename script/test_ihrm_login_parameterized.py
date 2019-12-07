import logging
import unittest
from parameterized import parameterized
import app
from api.login_api import LoginApi
from utils import assert_common, read_login_data


class TestIHRMLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #实例化api库的登录对象接口LoginApi
        cls.login_api = LoginApi()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass



    @parameterized.expand(read_login_data)
    def test_1_login_success(self,mobile,password,http_code,success,code,message):
        response = self.login_api.login(mobile,password)
        #日志打印返回对象的json数据，需要使用占位符操作
        logging.info("登录接口返回数据为{}".format(response.json()))
        #断言
        assert_common(self,response,http_code,success,code,message)