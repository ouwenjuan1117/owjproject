from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver


class TestTouchAction():
    def setup(self):
        desire_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "Displayed com.mumu.launcher",
            "appActivity": ".Launcher",
            # 不要停止被测应用程序的进程
            # "dontStopAppOnReset":"True",
            # # 跳过设备初始化，包括：安装和运行“设置”应用或权限设置，可用于提高启动性能
            # "skipDeviceInitialization": "true",
            # 启用Unicode输入，设置执行用例时的编码为中文
            "unicodeKeyboard": "true",
            # 在运行具有unicodeKeyboard功能的Unicode测试之后，将键盘重置为其原始状态
            "resetKeyboard": "true",
            # 在此会话之前，请勿重置应用程序状态
            "noReset": "true"
        }
        # 127.0.0.1:4723是启动appium server服务的地址      /wd/hub 是固定写法   desire_caps是要告诉server一些信息，需要测试的平台、设备、包等
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        # 建立连接以后，模拟器有点慢，加一个隐示等待
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        action = TouchAction(self.driver)
        action.press(x=244, y=374).wait(1000).move_to(x=711, y=374).wait(1000).move_to(x=1198, y=374).wait(
            1000).move_to(x=1198, y=1323).wait(200).release().perform()
