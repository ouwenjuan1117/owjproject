"""
添加成员页面
"""


class MamberInvitePage():

    def addcontact_menual(self):
        """
        添加成员页面有  手动输入添加
        :return: 添加成员编辑页面
        """
        # 局部导入 art + enter
        from Hogwarts.test_appium.pages.contact_edit_page import ContactEditPage
        return ContactEditPage()

    def goto_tosat(self):
        """
        封装一个tosat方法在添加成员页面
        :return:添加成功
        """
        return "添加成功"
