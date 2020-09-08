"""
添加成员编辑页面
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from Hogwarts.test_appium.pages.basepage import BasePage
from Hogwarts.test_appium.pages.mamber_invite_page import MamberInvitePage


class ContactEditPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    name_element = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
    gender_element = (MobileBy.XPATH, "//*[@text='男']")
    female_element = (MobileBy.XPATH, "//*[@text='女']")
    male_element = (MobileBy.XPATH, "//*[@text='男']")
    phonenum_element = (
    MobileBy.XPATH, "//*[contains(@text,'手机') and @class='android.widget.TextView']/..//*[@text='手机号']")
    save_element = (MobileBy.ID, "com.tencent.wework:id/gur")
    wait_element = (MobileBy.XPATH, "//*[@text='男']")
    def edit_name(self, name):
        """
        编辑姓名
        :return: 当前页面
        """
        # 定位到手机，通过先定位到 姓名 的父节点再定位到下面的输入框
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.find_and_sendkeys(self.name_element, name)
        return self

    def edit_gender(self, gender):
        """
        编辑性别
        :return: 当前页面
        """
        # 定位到性别
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # element = self.driver.find_element(MobileBy.XPATH, "//*[@text='男']")
        # if gender == '女':
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        # else:
        #     # 加入一个显示等待
        #     WebDriverWait(self.driver, 10).until(element).click()
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self.find_and_click(self.gender_element)
        if gender == "女":
            self.find_and_click(self.female_element)
        else:
            self.webdriverwait_click(self.wait_element)
            self.find_and_click(self.male_element)

        return self

    def edit_phonenum(self, phonenum):
        """
        编辑电话号码
        :return: 当前页面
        """
        # 定位到手机号码
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//*[contains(@text,'手机') and @class='android.widget.TextView']/..//*[@text='手机号']") \
        #     .send_keys(phonenum)
        self.find_and_sendkeys(self.phonenum_element, phonenum)
        return self

    def click_save(self):
        """
        点击保存
        :return: MamberInvitePage()添加成员页面
        """
        # 点击保存
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gur").click()
        self.find_and_click(self.save_element)
        sleep(2)
        return MamberInvitePage(self.driver)
