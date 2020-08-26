import pytest

from Hogwarts.test_selenium.test_project.pages.main_page import MainPage


class TestAddDepartment():

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    @pytest.mark.parametrize('dep_name', ['abs', '霍格沃兹', '人事部', '研发部'])
    def test_add_department(self, dep_name):
        # 1.从首页跳转到通讯页面  2.跳转到新建部门页面  3.添加部门   4.点击保存
        add_dep = self.main.go_to_contact().go_to_add_department().add_department(
            dep_name).save_department().get_dep_list()
        assert dep_name in add_dep

    def test_add_department_fail(self):
        # 1.从首页跳转到通讯页面  2.跳转到新建部门页面  3.添加部门   4.点击取消
        add_dep = self.main.go_to_contact().go_to_add_department().add_department(
            'Hogwarts').cancel_department().get_dep_list()
        assert 'Hogwarts' not in add_dep
