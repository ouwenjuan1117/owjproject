from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Hogwarts.test_appium.pages.basepage import BasePage
from Hogwarts.test_appium.pages.edit_member_page import EditMemberPage


class PersonalIofoPage(BasePage):
    """个人信息页面"""
    info_element = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guk']")
    edit_element = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def click_more(self):
        """
        点击更多
        :return:
        """
        # 进入个人信息页面
        # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guk']").click()
        self.find_and_click(self.info_element)
        return self

    def edit_member(self):
        """
        点击编辑成员
        :return: 进入编辑成员页面
        """
        # 点击 编辑成员
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.find_and_click(self.edit_element)
        return EditMemberPage(self.driver)
