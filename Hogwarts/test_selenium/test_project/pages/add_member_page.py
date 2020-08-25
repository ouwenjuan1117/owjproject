import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Hogwarts.test_selenium.test_project.pages.basepage import BasePage
from Hogwarts.test_selenium.test_project.pages.contact_page import ContactPage


class AddMemberPage(BasePage):

    def add_member(self):
        """添加成员"""

        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # cookie信息经常过期，等待10秒，然后手动扫码登录，之后把cookie信息，存入数据库
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('yxy')
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys('1234')
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys('12223234545')
        # 添加完之后还是在添加成员界面 所以返回的是self
        # return self 是为了实现返回当前页面时依然可以实现链式调用
        # 相当于别人调用是 add_member().save_member(),就等同于self.save_member()
        return self


    def save_member(self):
        '''定义一个保存的方法'''
        self.driver.find_element_by_xpath('//*[@id="js_contacts154"]/div/div[2]/div/div[4]/div/form/div[1]/a[2]')
        # 保存之后返回到通讯录界面
        return ContactPage()

    def cancel_member(self):
        '''定义一个取消保存的方法'''
        pass
