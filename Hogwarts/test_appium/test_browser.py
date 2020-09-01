from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestBrowser():
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "platformVersion": "6.0",
            "browserName": "Browser",
            "deviceName": "127.0.0.1:7555",
            "noReset": True
            # "appPackage": "io.appium.android.apis",
            # "appActivity": "io.appium.android.apis.view.PopupMenu1",
            # 工作引擎uiautomator2
            # "automationName":"uiautomator2",
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        # 建立连接以后，模拟器有点慢，加一个隐示等待
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)
