import requests


class Department:

    def create_department(self, token, department_id):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}"
        data = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": department_id
        }
        # 所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。所以在传请求体的时候尽量使用json参数
        r = requests.post(url=create_url, json=data)
        # return 获取到的响应体
        return r.json()

    def update_department(self, token, id):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}"
        data = {
            "id": id,
            "name": "hogwarts",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = requests.post(url=update_url, json=data)
        return r.json()

    def delete_department(self, token, department_id):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}&id={department_id}"
        data = {
            "errcode": 0,
            "errmsg": "deleted"
        }
        r = requests.post(url=delete_url, json=data)
        # print(r.json())
        return r.json()

    def get_department_list(self, token):
        get_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}"
        r = requests.get(url=get_department_url)
        return r.json()
