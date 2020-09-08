"""
basepage 基类
主要用老封装最基本的方法，初始化driver，find, 显示等待
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 初始化driver
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        """定义一个find方法，通过self.driver.find_element方式传入一个locator（默认是元祖类型），并且给它解包"""
        return self.driver.find_element(*locator)

    def finds(self, locator):
        """定义一个find方法，通过self.driver.find_elements方式传入一个locator（默认是元祖类型），并且给它解包"""
        return self.driver.find_elements(*locator)

    def find_and_click(self, locator):
        """定义一个查找元素并且点击的方法"""
        self.find(locator).click()

    def find_and_sendkeys(self, locator, value):
        """定义一个查找之后再输入的方法"""
        self.find(locator).send_keys(value)

    def find_by_scroll_and_click(self, text):
        """定义一个滚动查找的方法,传入的是一个文本信息"""
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector()'
                   '.scrollable(true).instance(0))'
                   '.scrollIntoView(new UiSelector()'
                   f'.text("{text}").instance(0));')
        self.find_and_click(element)

    def find_and_get_text(self, locator):
        """定义一个查找文本的方法"""
        return self.find(locator).text

    def gettosat_text(self):
        """定义一个tosat方法"""
        element = (MobileBy.XPATH, "//*[@text='添加成功']")
        # mytoast = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").text
        return self.find_and_get_text(element)

    def webdriverwait_click(self, locator):
        return WebDriverWait(self.driver, 10).until(self.find(locator)).click()
        #     # 加入一个显示等待
        #     WebDriverWait(self.driver, 10).until(element).click()
