import logging
import unittest

import pymysql

import app
from api.employee_api import EmployeeApi
from utils import assert_common, DBUtils


class TestEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.employee_api = EmployeeApi()

    def test_1_add_emp(self):
        logging.info("hello")
        response = self.employee_api.add_emp("哪吒你好4","15013345671")
        logging.info("添加员工{}".format(response.json()))
        assert_common(self,response,200,True,10000,"操作成功")
        jsonData = response.json()
        emp_id = jsonData.get('data').get('id')
        app.EMPID = emp_id
        logging.info("保存的员工ID：{}".format(app.EMPID))

    def test_2_query_emp(self):
         response = self.employee_api.query_emp()
         logging.info("查询员工接口返回的数据为:{}".format(response.json()))
         assert_common(self,response,200,True,10000,'操作成功')

    def test_3_modify_emp(self):
        response = self.employee_api.modify_emp("奥特曼和小怪物")
        logging.info("修改员工接口返回的数据为：{}".format(response.json()))
        assert_common(self,response,200,True,10000,"操作成功")
        #断言数据库中的数据
        # conn = pymysql.connect("182.92.81.159","readuser",'iHRM_user_2019','ihrm')
        # #获取游标
        # cursor = conn.cursor()
        # #执行查询语句
        # query_sql = 'select username from bs_user where id = {} '.format(app.EMPID)
        # cursor.execute(query_sql)
        # result = cursor.fetchone()
        # cursor.close()
        # conn.close()
        # logging.info("----查询数据库中员工id为{}的username是{} ".format(app.EMPID,result[0]))
        # #断言数据库中返回的数据
        # self.assertEqual("奥特曼和小怪物",result[0])
        with DBUtils("182.92.81.159","readuser","iHRM_user_2019","ihrm") as db:
            query_sql = 'select username from bs_user where id ={} limit 1 '.format(app.EMPID)
            db.execute(query_sql)
            result = db.fetchone()
            logging.info("haha ")

        logging.info("----查询数据库中员工id为{}的username是{}".format(app.EMPID,result[0]))
        logging.info("haha1 ")
        #断言数据库中返回的数据
        self.assertEqual("奥特曼和小怪物",result[0])

    def test_4_delete_emp(self):
        response = self.employee_api.delete_emp()
        logging.info("删除员工接口返回的数据：{}".format(response.json()))
        assert_common(self,response,200,True,10000,'操作成功')