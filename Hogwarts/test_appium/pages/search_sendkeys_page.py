from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Hogwarts.test_appium.pages.basepage import BasePage
from Hogwarts.test_appium.pages.personal_iofo_page import PersonalIofoPage
from Hogwarts.test_appium.pages.search_info_page import SearchInfoPage


class SearchSendkeys(BasePage):
    '''
    点击搜索框，进入输入搜索成员界面
    '''
    search_element = (MobileBy.XPATH, "//*[@text='搜索']")

    def search_sendkeys(self, membername):
        """在搜索框中，输入需要搜索的成员"""
        # 定位到搜索输入框
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(membername)
        self.find_and_sendkeys(self.search_element, membername)
        sleep(3)
        return SearchInfoPage(self.driver)
