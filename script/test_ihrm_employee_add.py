import logging
import unittest
import requests

from api.login_api import LoginApi
headers = {}
user_id = None


class TestIHRMEmployee(unittest.TestCase):
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
        response = self.login_api.login("13800000002", "123456")
        data = response.json().get("data")
        data = 'Bearer ' + data
        print(data)
        logging.info("登录接口返回数据为{}".format(response.json()))
        global headers
        headers = {"Content-Type":"application/json",'Authorization':data}
        print(headers)
        add_data = {"username":"小徐262982","mobile":"13923941814","timeOfEntry":"2019-11-05","formOfEmployment":1,"workNumber":"111","departmentName":"财务部",
                     "departmentId":"1066238836272664576","correctionTime":"2019-11-29T16:00:00.000Z"}
        response = requests.post(url="http://182.92.81.159/api/sys/user",json=add_data,headers=headers)
        print(response.json())
        self.assertEqual(True,response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertEqual("操作成功！",response.json().get("message"))
        global user_id
        jsonData = response.json().get("data")
        user_id = jsonData.get("id")
        print(user_id)

