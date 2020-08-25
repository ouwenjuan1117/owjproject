from Hogwarts.test_selenium.test_project.pages.basepage import BasePage


class ContactPage():

    def go_to_add_member(self):
        # 解决循环导入报错的问题
        from Hogwarts.test_selenium.test_project.pages.add_member_page import AddMemberPage

        '''点击添加成员'''
        # 对 addmemberpage 类进行实例化,表示业务逻辑的转换关系
        return AddMemberPage()
