import logging
import unittest
from parameterized import parameterized

import app
from api.login_api import LoginApi
from utils import assert_common


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



    def test_1_login_success(self,):
        response = self.login_api.login("13800000002","123456")
        #日志打印返回对象的json数据，需要使用占位符操作
        logging.info("登录接口返回数据为{}".format(response.json()))
        #断言
        assert_common(self,response,200,True,10000,'操作成功')
        #获取json数据
        jsonData = response.json()
        #拼接token组成全局变量
        token = 'Bearer ' + jsonData.get('data')
        #把token保存到全局变量app.py中
        app.HEADERS ={"Content-Type":"application/json",'Authorization':token}
        logging.info("保存的的登录token{}".format(app.HEADERS))

    # def test_2_mobile_is_error(self):
    #     response = self.login_api.login("13900000002","123456")
    #     #日志打印返回对象的json数据，需要使用占位符操作
    #     logging.info("登录接口返回数据为{}".format(response.json()))
    #     #断言
    #     assert_common(self,response,200,False,20001,'用户名或密码错误')
    #
    # def test_3_password_is_error(self):
    #     response = self.login_api.login("13800000002","12345634")
    #     #日志打印返回对象的json数据，需要使用占位符操作
    #     logging.info("登录接口返回数据为{}".format(response.json()))
    #     #断言
    #     assert_common(self,response,200,False,20001,'用户名或密码错误')
    #
    # def test_4_none_params(self):
    #     response = self.login_api.login_none_params()
    #     #日志打印返回对象的json数据，需要使用占位符操作
    #     logging.info("登录接口返回数据为{}".format(response.json()))
    #     #断言
    #     assert_common(self,response,200,False,99999,'抱歉')
    #
    # def test_5_mobile_is_none(self):
    #     response = self.login_api.login("","error")
    #     #日志打印返回对象的json数据，需要使用占位符操作
    #     logging.info("登录接口返回数据为{}".format(response.json()))
    #     #断言
    #     assert_common(self,response,200,False,20001,'用户名或密码错误')
    #
    # def test_6_password_is_none(self):
    #     response = self.login_api.login("13800000002","")
    #     #日志打印返回对象的json数据，需要使用占位符操作
    #     logging.info("登录接口返回数据为{}".format(response.json()))
    #     #断言
    #     assert_common(self,response,200,False,20001,'用户名或密码错误')
    #
    # def test_7_extra_params(self):
    #     response = self.login_api.login_extra_params()
    #     #日志打印返回对象的json数据，需要使用占位符操作
    #     logging.info("登录接口返回数据为{}".format(response.json()))
    #     #断言
    #     assert_common(self,response,200,True,10000,'操作成功')
    #
    # def test_8_less_params(self):
    #     response = self.login_api.login_less_params()
    #     #日志打印返回对象的json数据，需要使用占位符操作
    #     logging.info("登录接口返回数据为{}".format(response.json()))
    #     #断言
    #     assert_common(self,response,200,False,99999,"抱歉")