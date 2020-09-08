"""
通讯录页面
"""
from appium.webdriver.common.mobileby import MobileBy

from Hogwarts.test_appium.pages.basepage import BasePage
from Hogwarts.test_appium.pages.mamber_invite_page import MamberInvitePage


class AddressListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    addmember_text = "添加成员"
    def add_member(self):
        """
        通讯录页面可以进入到 添加成员页面
        :return: 添加成员页面
        """
        # 点击 添加成员，当成员很多时不会显示在第一页，需要滑动到最后
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()
        self.find_by_scroll_and_click(self.addmember_text)
        return MamberInvitePage(self.driver)

    search_click_element = (MobileBy.ID, "com.tencent.wework:id/guu")

    def goto_click_search(self):
        """
        定义一个方法，叫点击搜索框
        :return: 返回到输入搜索成员界面
        """
        from Hogwarts.test_appium.pages.search_sendkeys_page import SearchSendkeys
        # 定位到 搜索
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guu").click()
        self.find_and_click(self.search_click_element)
        return SearchSendkeys(self.driver)
