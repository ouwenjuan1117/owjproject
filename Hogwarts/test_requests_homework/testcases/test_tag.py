import yaml
from jsonpath import jsonpath

from Hogwarts.test_requests_homework.api.tag_management import TagManagement


class TestTag:

    def setup_class(self):
        # 实例化TagManagement()
        self.tagmanagement = TagManagement()
        config_info = yaml.safe_load(open("config.yaml"))
        # 直接通过实例化TagManagement()调用get_token()函数
        self.tagmanagement.get_token(config_info["token"]["tag_secret"])

    def test_create_tag(self):
        self.tagmanagement.create_tag(1)
        list = self.tagmanagement.get_tag_list()
        print(list)
        name = jsonpath(list, "$..tagname")
        assert 'hogwarts' in name
        # assert list['taglist'][0]['tagname'] == 'hogwarts'

    def test_update_tag(self):
        self.tagmanagement.update_tag(1)
        list = self.tagmanagement.get_tag_list()
        # print(list)
        name = jsonpath(list, "$..tagname")
        assert '广州研发中心' in name
        # assert list['taglist'][0]['tagname'] == '广州研发中心'

    def test_delete_tag(self):
        self.tagmanagement.delete_tag(1)
        list = self.tagmanagement.get_tag_list()
        print(list)
        assert len(list['taglist']) == 0

    def test_get_department_list(self):
        self.tagmanagement.get_tag_list()
