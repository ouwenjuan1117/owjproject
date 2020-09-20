# 创建部门成功->更新部门成功->删除部门成功（业务场景校验）
import requests

class TestDepartment:
    def setup_class(self):
        """每次执行前，需要先获取token信息"""
        # 每个企业都拥有唯一的corpid，获取此信息可在管理后台“我的企业”－“企业信息”
        corp_id = "ww9c9dfb3253386139"
        # # 获取通讯录管理secret，在“管理工具”-“通讯录同步”里面查看
        corp_secret = "ow77plErSKg8EbcJ5n6kPcioaqpgZbGeCoT063nn1Ow"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.get(url=token_url)
        # 获取到接口的响应体
        # print(r.json())
        self.token = r.json()["access_token"]

    def test_create_department(self):
        """
        创建部门
        通讯录api默认只有只读权限，需手动设置为可编辑状态 （管理工具->通讯录同步）
        """
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        data ={
               "name": "广州研发中心",
               "name_en": "RDGZ",
               "parentid": 1,
               "order": 1,
               "id": 2
            }
        # 所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。所以在传请求体的时候尽量使用json参数
        r = requests.post(url=create_url,json=data)
        print(r.json())
        # 创建部门是否成功，需要获取部门列表去校验是否创建成功,id非必填项，可以不填
        # 调用查询部门列表接口，获取部门列表信息
        get_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_url)
        # print(list.json())
        # 通过得到查询部门列表接口的返回值，实现查询部门是否创建成功
        assert list.json()['department'][1]['name'] == '广州研发中心'
        assert r.json()["errmsg"] == 'created'



    def test_update_department(self):
        """
        修改部门名称
        """
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data ={
               "id": 2,
               "name": "hogwarts",
               "name_en": "RDGZ",
               "parentid": 1,
               "order": 1
            }
        r = requests.post(url=update_url,json=data)
        print(r.json())
        get_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_url)
        # print(list.json())
        assert list.json()['department'][1]['name'] == 'hogwarts'
        assert r.json()["errmsg"] == 'updated'



    def test_delete_department(self):
        """
        删除部门信息
        """
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id=2"
        data ={
               "errcode": 0,
               "errmsg": "deleted"
            }
        r = requests.post(url=delete_url,json=data)
        print(r.json())
        get_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_url)
        # 删除之后，列表的长度为1
        assert len(list.json()['department']) == 1
        assert r.json()["errmsg"] == 'deleted'
