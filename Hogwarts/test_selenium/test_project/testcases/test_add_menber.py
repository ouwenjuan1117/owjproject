import time

import pytest

from Hogwarts.test_selenium.test_project.pages.main_page import MainPage


class TestAddMember:

    def setup(self):
        self.main = MainPage()

    @pytest.mark.run(order=1)
    def test_add_member(self):
        # 1.从首页跳转到添加成员页面  2.添加成员页面  3.点击保存
        namelist = self.main.go_to_add_member().add_member("杨小杨", "5555", "13345459999").save_member().get_member_list()
        assert "杨小杨" in namelist


    @pytest.mark.run(order=2)
    # 有成功的用例就会有失败的用例
    def test_add_member_fail(self):
        namelist = self.main.go_to_add_member().add_member("杨小杨2", "5555",
                                                           "13345459999").cancel_member().get_member_list()
        assert "杨小杨2" not in namelist


    @pytest.mark.run(order=3)
    def test_contact_member(self):
        # 1.从首页跳转到通讯页面  2.跳转到添加成员页面  3.添加成员页面
        self.main.go_to_contact().go_to_add_member().add_member("杨小杨3", "5553",
                                                                "15345458888").save_member().get_member_list()


    def teardown(self):
        self.main.driver.quit()
