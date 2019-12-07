import requests
class LoginApi:
    def __init__(self):
        #初始化登录url
        self.login_url = "http://182.92.81.159" + "/api/sys/login"
        self.headers = {"Content-Type":"application/json"}
    def login(self,mobile,password):
        login_data = {"mobile":mobile,"password":password}
        return requests.post(url=self.login_url,json=login_data,headers=self.headers)

    def login_none_params(self):
        return requests.post(url=self.login_url, headers=self.headers)

    def login_extra_params(self):
        return requests.post(url=self.login_url,
                             json={"mobile":"13800000002","password":"123456","extra_params":"测试"},
                             headers=self.headers)

    def login_less_params(self):
        return requests.post(url=self.login_url,
                             json={"mobile":"13800000002"},
                             headers=self.headers)