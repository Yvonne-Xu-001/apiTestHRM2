#1导包
import unittest

import time

from app import BASE_DIR
from script.test_ihrm_emp import TestEmp
from script.test_ihrm_emp_parameterized import TestEmpParameterized
from script.test_ihrm_login import TestIHRMLogin
#2实例化测试套件
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
#3添加测试用例
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestEmpParameterized))
#4定义文件的路径和名称
file_path = BASE_DIR + '/report/ihrm.html'
#5打开文件
with open(file_path,mode='wb') as f:
    #6实例化HTMLTestRunner
    runner = HTMLTestRunner(f,verbosity=1,title='ihrm测试报告',description='ihrm登录接口和人员管理模块测试')
    #7运行
    runner.run(suite)
