"""
添加成员页面
"""
from appium.webdriver.common.mobileby import MobileBy

from Hogwarts.test_appium.pages.basepage import BasePage


class MamberInvitePage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    addmember_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    def addcontact_menual(self):
        """
        添加成员页面有  手动输入添加
        :return: 添加成员编辑页面
        """
        # 局部导入 art + enter
        from Hogwarts.test_appium.pages.contact_edit_page import ContactEditPage
        # 点击 手动输入添加
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click(self.addmember_element)
        return ContactEditPage(self.driver)

    def goto_tosat(self):
        """
        封装一个tosat方法在添加成员页面
        :return:添加成功
        """
        # 打印下页面布局，看布局下有没有 toast
        # print(self.driver.page_source)
        # mytoast = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").text
        mytoast = self.gettosat_text()
        return mytoast
