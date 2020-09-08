from appium.webdriver.common.mobileby import MobileBy

from Hogwarts.test_appium.pages.basepage import BasePage
from Hogwarts.test_appium.pages.personal_iofo_page import PersonalIofoPage


class SearchInfoPage(BasePage):
    """
    搜索到成员界面
    """

    def search_sendkeys_click(self, membername):
        """
        点击搜索到的成员
        :param membername:
        :return: 进入个人信息界面
        """
        text_element = (MobileBy.XPATH, f"//*[@text='{membername}']")
        # 判断成员是否存在，存在的话 membername文本应该为2，不存在的话那就只有一个membername(老师写的方式)
        # eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{membername}']")
        eles = self.finds(text_element)
        beforenum = len(eles)
        if beforenum < 2:
            print("没有可删除人员")
            # return 不进行后面的操作
            return
        # 否则的话，继续往下走，找到第二个进行点击操作
        eles[1].click()
        return PersonalIofoPage(self.driver)

    def goto_determine_del(self, membername):
        determine_element = (MobileBy.XPATH, f"//*[@text='{membername}']")
        # 判断是否删除成功
        # eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{membername}']")
        eles1 = self.finds(determine_element)
        return len(eles1)
