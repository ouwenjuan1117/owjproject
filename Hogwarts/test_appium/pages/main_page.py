"""
创建一个首页
主页：到通讯录，到工作台
"""
from Hogwarts.test_appium.pages.addresslist_page import AddressListPage


class MainPage:
    # 进入到通讯录
    def goto_addresslist(self):
        """
        点击通讯录
        :return: 通讯录界面
        """
        return AddressListPage()

    # 进入到工作台
    def goto_workbench(self):
        pass
