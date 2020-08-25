import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Hogwarts.test_selenium.test_project.pages.add_member_page import  AddMemberPage
from Hogwarts.test_selenium.test_project.pages.basepage import BasePage
from Hogwarts.test_selenium.test_project.pages.contact_page import ContactPage


class MainPage(BasePage):
    '''点击通讯录'''

    def go_to_contact(self):
        # 对 contactpage 类进行实例化,表示业务逻辑的转换关系
        return ContactPage()

    def go_to_add_member(self):
        '''点击添加成员'''
        # self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # cookie信息经常过期，等待10秒，然后手动扫码登录，之后把cookie信息，存入数据库
        time.sleep(2)
        res = self.driver.find_element_by_id("check_corp_info")
        print(res)
        print(res.text)
        e = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[1]/div[4]/div[2]/a[1]')
        print(e)
        print(e.text)
        e.click()
        # 对addmemberpage 类进行实例化,表示业务逻辑的转换关系
        return AddMemberPage()
