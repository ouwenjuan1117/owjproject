import requests

from Hogwarts.test_requests.api.wework import WeWork


class Department(WeWork):
    # 未封装requests之前的代码
    # def create_department(self, department_id):
    #     create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
    #     data = {
    #         "name": "广州研发中心",
    #         "name_en": "RDGZ",
    #         "parentid": 1,
    #         "order": 1,
    #         "id": department_id
    #     }
    #     # 所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。所以在传请求体的时候尽量使用json参数
    #     # r = requests.post(url=create_url, json=data)
    #     # return 获取到的响应体
    #     return r.json()
    #
    # def update_department(self, department_id):
    #     update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
    #     data = {
    #         "id": department_id,
    #         "name": "hogwarts",
    #         "name_en": "RDGZ",
    #         "parentid": 1,
    #         "order": 1
    #     }
    #     # r = requests.post(url=update_url, json=data)
    #     return r.json()
    #
    # def delete_department(self, department_id):
    #     delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}"
    #     data = {
    #         "errcode": 0,
    #         "errmsg": "deleted"
    #     }
    #     r = requests.post(url=delete_url, json=data)
    #     # print(r.json())
    #     return r.json()
    #
    # def get_department_list(self):
    #     get_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
    #     r = requests.get(url=get_department_url)
    #     return r.json()

    # 封装requests之后的代码
    def create_department(self, department_id):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": department_id
        }
        # get_token的请求信息
        req = {
            "method": "post",
            "url": create_url,
            "json": data
        }
        # 继承BaseApi之后，调用send_requests方法
        r = self.send_requests(req)
        # 所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。所以在传请求体的时候尽量使用json参数
        # r = requests.post(url=create_url, json=data)
        # return 获取到的响应体
        return r.json()

    def update_department(self, department_id):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data = {
            "id": department_id,
            "name": "hogwarts",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        # get_token的请求信息
        req = {
            "method": "post",
            "url": update_url,
            "json": data
        }
        # 继承BaseApi之后，调用send_requests方法
        r = self.send_requests(req)
        # r = requests.post(url=update_url, json=data)
        return r.json()

    def delete_department(self, department_id):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}"
        data = {
            "errcode": 0,
            "errmsg": "deleted"
        }
        # get_token的请求信息
        req = {
            "method": "post",
            "url": delete_url,
            "json": data
        }
        # 继承BaseApi之后，调用send_requests方法
        r = self.send_requests(req)
        # r = requests.post(url=delete_url, json=data)
        # print(r.json())
        return r.json()

    def get_department_list(self):
        get_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        # get_token的请求信息
        req = {
            "method": "get",
            "url": get_department_url
        }
        # 继承BaseApi之后，调用send_requests方法
        r = self.send_requests(req)
        # r = requests.get(url=get_department_url)
        return r.json()
