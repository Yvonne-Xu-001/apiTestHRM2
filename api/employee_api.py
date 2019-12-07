import requests
import app


class EmployeeApi():
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"
        self.check_url = "http://182.92.81.159/api/sys/user?page=1&size=10"
        self.emp_url = "http://182.92.81.159/api/sys/user"
    # def login(self,obj,mobile,password):
    #     return obj.post(self.login_url,
    #                              json={"mobile": mobile, "password": password})
    # def check(self,obj):
    #     return obj.get(self.check_url)
    def add_emp(self,username,mobile):
        data = {"username":username,"mobile":mobile,"timeOfEntry":"2019-11-05","formOfEmployment":1,"workNumber":"111","departmentName":"财务部",
                     "departmentId":"1066238836272664576","correctionTime":"2019-11-29T16:00:00.000Z"}
        print(app.HEADERS)
        #发送修改请求
        return requests.post(self.emp_url,json=data,headers=app.HEADERS)

    def query_emp(self):
        #拼接要查询员工url
        query_emp_url = self.emp_url + "/" + app.EMPID
        #发送查询请求
        return requests.get(query_emp_url,headers=app.HEADERS)

    def modify_emp(self,username):
        #拼接要发送的修改员工的url
        modify_emp_url = self.emp_url + "/" + app.EMPID
        #发送修改请求
        return requests.put(modify_emp_url,json={"username":username},headers=app.HEADERS)

    def delete_emp(self):
        delete_emp_url = self.emp_url + '/' + app.EMPID
        return requests.delete(delete_emp_url,headers=app.HEADERS)
