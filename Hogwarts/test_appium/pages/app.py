"""
用来存放app端特有的操作
比如：启动应用，关闭应用，重启应用，进入到首页
"""
from appium import webdriver

from Hogwarts.test_appium.pages.basepage import BasePage
from Hogwarts.test_appium.pages.main_page import MainPage


class App(BasePage):
    def start(self):
        """
        启动应用
        :return:
        """
        if self.driver == None:
            # 如果为None的时候，创建一个新的driver，否则的话，复用之前的driver
            desire_caps = {
                "platformName": "android",
                "platformVersion": "6.0",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "settings[waitForIdleTimeout]": 0,
                # 在此会话之前，请勿重置应用程序状态,不要清空缓存
                "noReset": 'true'
            }
            # desire_caps是要告诉server一些信息，需要测试的平台、设备、包等
            # 127.0.0.1:4723是启动appium server服务的地址      /wd/hub 是固定写法
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
            # 建立连接以后，模拟器有点慢，加一个隐示等待
            self.driver.implicitly_wait(20)
        else:
            # launch_app将我们appPackage，appActivity自动的启用起来，不需要做其他初始化操作，启动desire_caps设置的appPackage，appActivity应用
            # self.driver.start_activity() 用这个方法去启动也是可以的，但是需要传两个参数appPackage，appActivity，可以启动任何页面的应用
            self.driver.launch_app()
        return self

    def restaet(self):
        """
        重启应用
        :return:
        """
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        """
        关闭应用
        :return:
        """
        self.driver.quit()

    def goto_main(self) -> MainPage:
        """
        进入到主页
        :return:返回到主页面
        """
        return MainPage(self.driver)
