import time
from selenium.webdriver.common.by import By

from Hogwarts.test_selenium.test_project.pages.basepage import BasePage
from Hogwarts.test_selenium.test_project.pages.contact_page import ContactPage


class AddMemberPage(BasePage):
    # 参数是一个元祖
    _username = (By.XPATH, "//*[@id='username']")
    _cancel = (By.CSS_SELECTOR, "[node-type='cancel']")

    def add_member(self, name, acc_id, phone):
        """添加成员"""
        time.sleep(1)
        # *self.username代表的是解元祖，类属性，通过self.调用,_表示私有
        self.find(*self._username).send_keys(name)
        # 为了实现将来技术栈更换，所有的都换成定义的方法，到时候只需要改find方法就可以了
        self.find(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys(acc_id)
        self.find(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys(phone)
        # 添加完之后还是在添加成员界面 所以返回的是self
        # return self 是为了实现返回当前页面时依然可以实现链式调用
        # 相当于别人调用是 add_member().save_member(),就等同于self.save_member()
        return self


    def save_member(self):
        '''定义一个保存的方法'''
        self.find(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save').click()
        # 保存之后返回到通讯录界面
        return ContactPage(self.driver)

    def cancel_member(self):
        '''定义一个取消保存的方法'''
        self.find(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_cancel").click()
        self.wait_for_clickable(self._cancel)
        self.find(*self._cancel).click()
        return ContactPage(self.driver)
