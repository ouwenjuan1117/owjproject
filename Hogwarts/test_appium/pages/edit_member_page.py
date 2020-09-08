from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from Hogwarts.test_appium.pages.basepage import BasePage


class EditMemberPage(BasePage):
    """
    编辑成员页面
    """
    del_text = "删除成员"
    determine_element = (MobileBy.XPATH, "//*[@text='确定']")

    def del_member(self, membername):
        """
        点击删除成员
        :return:返回搜索页面
        """
        element = (MobileBy.XPATH, f"//*[@text='{membername}']")
        from Hogwarts.test_appium.pages.search_sendkeys_page import SearchSendkeys
        # 点击删除成员
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("删除成员").instance(0));').click()
        self.find_by_scroll_and_click(self.del_text)
        # 点击 确定 删除
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        self.find_and_click(self.determine_element)
        sleep(3)
        from Hogwarts.test_appium.pages.search_info_page import SearchInfoPage
        return SearchInfoPage(self.driver)
