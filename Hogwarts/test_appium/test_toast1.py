from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast():
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.view.PopupMenu1",
            # 工作引擎uiautomator2
            "automationName": "uiautomator2"
            # "noReset": True
        }
        # 127.0.0.1:4723是启动appium server服务的地址      /wd/hub 是固定写法   desire_cap是要告诉server一些信息，需要测试的平台、设备、包等
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        # 建立连接以后，模拟器有点慢，加一个隐示等待
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        # 打印一下当前页面，看一下有没有toast元素
        # print(self.driver.page_source)
        # 定位到toast弹出来的文本信息（方式1）
        # print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        # 通过文本信息来定位（方式2）
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup')]").text)
