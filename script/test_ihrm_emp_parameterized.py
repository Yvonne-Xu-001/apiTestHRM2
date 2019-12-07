import logging
import unittest

import pymysql
from parameterized import parameterized

import app
from api.employee_api import EmployeeApi
from utils import assert_common, DBUtils, read_add_emp_data, read_query_emp_data, read_modify_emp_data, \
    read_delete_emp_data


class TestEmpParameterized(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.employee_api = EmployeeApi()

    @parameterized.expand(read_add_emp_data)
    def test_1_add_emp(self,username,mobile,http_code,success,code,message):
        logging.info("hello")
        response = self.employee_api.add_emp(username,mobile)
        logging.info("添加员工{}".format(response.json()))
        assert_common(self,response,http_code,success,code,message)
        jsonData = response.json()
        emp_id = jsonData.get('data').get('id')
        app.EMPID = emp_id
        logging.info("保存的员工ID：{}".format(app.EMPID))

    @parameterized.expand(read_query_emp_data)
    def test_2_query_emp(self,http_code,success,code,message):
         response = self.employee_api.query_emp()
         logging.info("查询员工接口返回的数据为:{}".format(response.json()))
         assert_common(self,response,http_code,success,code,message)

    @parameterized.expand(read_modify_emp_data)
    def test_3_modify_emp(self,username,http_code,success,code,message):
        response = self.employee_api.modify_emp(username)
        logging.info("修改员工接口返回的数据为：{}".format(response.json()))
        assert_common(self,response,http_code,success,code,message)
        with DBUtils("182.92.81.159","readuser","iHRM_user_2019","ihrm") as db:
            query_sql = 'select username from bs_user where id ={} limit 1 '.format(app.EMPID)
            db.execute(query_sql)
            result = db.fetchone()
            logging.info("haha ")
        logging.info("----查询数据库中员工id为{}的username是{}".format(app.EMPID,result[0]))
        logging.info("haha1 ")
        #断言数据库中返回的数据
        self.assertEqual(username,result[0])

    @parameterized.expand(read_delete_emp_data)
    def test_4_delete_emp(self,http_code,success,code,message):
        response = self.employee_api.delete_emp()
        logging.info("删除员工接口返回的数据：{}".format(response.json()))
        assert_common(self,response,http_code,success,code,message)