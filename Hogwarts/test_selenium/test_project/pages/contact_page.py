import time
from selenium.webdriver.common.by import By
from Hogwarts.test_selenium.test_project.pages.basepage import BasePage


class ContactPage(BasePage):
    _add_member = (By.CSS_SELECTOR, ".ww_operationBar .qui_btn.ww_btn.js_add_member")
    _add_department_button = (
    By.CSS_SELECTOR, ".member_colLeft_top_addBtnWrap.js_create_dropdown .member_colLeft_top_addBtn")
    _add_department = (By.CSS_SELECTOR, ".js_create_party")
    def go_to_add_member(self):
        # 解决循环导入报错的问题
        from Hogwarts.test_selenium.test_project.pages.add_member_page import AddMemberPage
        time.sleep(10)
        self.find(*self._add_member).click()

        '''点击添加成员'''
        # 对 addmemberpage 类进行实例化,表示业务逻辑的转换关系
        return AddMemberPage(self.driver)

    def get_member_list(self):
        # 拿到所以的员工名单信息
        # find_element和find_elements的区别在于，find_elements返回的是一个列表，find_element返回的是一个元素
        ele = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # print(ele)
        return [name.text for name in ele]
        # list1=[]
        # for name in ele:
        #     list1.append(name.text)
        # print(list1)

    def get_dep_list(self):
        time.sleep(5)
        dep_ele = self.finds(By.CSS_SELECTOR, '.jstree-anchor')
        return [name.text for name in dep_ele]

    def go_to_add_department(self):
        from Hogwarts.test_selenium.test_project.pages.department_page import DepartmentPage
        # self.find(By.XPATH,'//*[@id="js_contacts413"]/div/div[1]/div/div[1]/a')
        # 定位到添加部门‘+’按钮
        self.find(*self._add_department_button).click()
        # 定位到点击添加部门
        self.find(*self._add_department).click()
        return DepartmentPage(self.driver)
