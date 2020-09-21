import yaml
from jsonpath import jsonpath

from Hogwarts.test_requests.api.department import Department


class TestDepartment:

    def setup_class(self):
        # 实例化WeWork()
        # wework = WeWork()
        # 实例化Department
        self.department = Department()
        # 直接读取yaml文件中红的corp_secret
        config_info = yaml.safe_load(open("config.yaml"))
        # self.token = wework.get_token()
        # 继承之后就不需要实例化wework = WeWork()，直接通过实例化的self.department调用get_token()函数
        # 通过传入不同的secret获取不同的token权限，给不同的业务测试用例使用
        self.department.get_token(config_info["token"]["department_secret"])  # 读取到yaml文件中的department_secret

    def test_create_department(self):
        self.department.create_department(3)
        list = self.department.get_department_list()
        name = jsonpath(list, "$..name")
        assert '广州研发中心' in name
        # assert list['department'][1]['name'] == '广州研发中心'


    def test_update_department(self):
        self.department.update_department(3)
        list = self.department.get_department_list()
        name = jsonpath(list, "$..name")
        assert 'hogwarts' in name
        # assert list['department'][1]['name'] == 'hogwarts'

    def test_delete_department(self):
        self.department.delete_department(3)
        list = self.department.get_department_list()
        department_id = jsonpath(list, "$..id")
        assert 3 not in department_id
        # assert len(list['department']) == 1

    def test_get_department_list(self):
        self.department.get_department_list()
