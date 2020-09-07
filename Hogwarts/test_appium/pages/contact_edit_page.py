"""
添加成员编辑页面
"""
from Hogwarts.test_appium.pages.mamber_invite_page import MamberInvitePage


class ContactEditPage():
    def edit_name(self, name):
        """
        编辑姓名
        :return: 当前页面
        """
        return self

    def edit_gender(self, gender):
        """
        编辑性别
        :return: 当前页面
        """
        return self

    def edit_phonenum(self, phonenum):
        """
        编辑电话号码
        :return: 当前页面
        """
        return self

    def click_save(self):
        """
        点击保存
        :return: MamberInvitePage()添加成员页面
        """
        return MamberInvitePage()
