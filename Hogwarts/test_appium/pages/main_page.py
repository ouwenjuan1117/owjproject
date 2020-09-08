"""
创建一个首页
主页：到通讯录，到工作台
"""
from appium.webdriver.common.mobileby import MobileBy

from Hogwarts.test_appium.pages.addresslist_page import AddressListPage
from Hogwarts.test_appium.pages.basepage import BasePage


class MainPage(BasePage):
    # 通讯录
    addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")
    # 进入到通讯录
    def goto_addresslist(self):
        """
        点击通讯录
        :return: 通讯录界面
        """
        # 定位到通讯录，并做点击操作
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()

        # 调用BasePage的find_and_click方法，传入一个locator参数
        self.find_and_click(self.addresslist_element)
        return AddressListPage(self.driver)

    # 进入到工作台
    def goto_workbench(self):
        pass
