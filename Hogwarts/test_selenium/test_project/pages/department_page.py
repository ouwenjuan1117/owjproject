from time import sleep
from selenium.webdriver.common.by import By
from Hogwarts.test_selenium.test_project.pages.basepage import BasePage


class DepartmentPage(BasePage):

    def add_department(self, dep_name):
        # 定位到添加部门界面中的新建部门的部门名称输入框
        self.find(By.CSS_SELECTOR, '[name=name]').send_keys(dep_name)
        # 选择所在部门
        self.find(By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list').click()
        # 选择获取到列表的第一个元素
        dep_list = self.finds(By.CSS_SELECTOR,
                              '.qui_dropdownMenu.ww_dropdownMenu.member_colLeft.js_party_list_container')
        # print(dep_list)
        # for i in dep_list:
        #     print(i)
        if dep_list is not None:
            dep_list[0].click()
        sleep(2)
        return self

    def save_department(self):
        '''定义一个保存的方法'''
        from Hogwarts.test_selenium.test_project.pages.contact_page import ContactPage
        # 点击确定按钮
        self.find(By.CSS_SELECTOR, "#__dialog__MNDialog__ [d_ck=\"submit\"]").click()
        return ContactPage(self.driver)

    def cancel_department(self):
        '''定义一个取消保存的方法'''
        from Hogwarts.test_selenium.test_project.pages.contact_page import ContactPage
        # 点击取消按钮
        self.find(By.CSS_SELECTOR, "#__dialog__MNDialog__ [d_ck=\"cancel\"]").click()
        return ContactPage(self.driver)
