"""
通讯录页面
"""
from Hogwarts.test_appium.pages.mamber_invite_page import MamberInvitePage


class AddressListPage():
    def add_member(self):
        """
        通讯录页面可以进入到 添加成员页面
        :return: 添加成员页面
        """
        return MamberInvitePage()
