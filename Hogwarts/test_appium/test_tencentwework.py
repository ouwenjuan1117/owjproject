from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestTencentWework:
    def setup(self):
        desire_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "settings[waitForIdleTimeout]": 0,
            # 在此会话之前，请勿重置应用程序状态
            "noReset": 'true'
        }
        # desire_caps是要告诉server一些信息，需要测试的平台、设备、包等
        # 127.0.0.1:4723是启动appium server服务的地址      /wd/hub 是固定写法
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        # 建立连接以后，模拟器有点慢，加一个隐示等待
        self.driver.implicitly_wait(20)

    def teardown(self):
        # 返回上一步操作
        # self.driver.back()
        self.driver.quit()

    def test_wework_daka(self):
        """
        打卡测试用例
        :return:
        """
        # 在主界面定位到 工作台
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 向下滑动 找到打卡 并且对它完成点击操作
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        sleep(5)
        # 定位到外出打卡界面
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ghc").click()
        # 定位到打卡按钮  contains 包含于
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/alq").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"次外出")]').click()
        # 定位到外出打卡文本信息
        rrsult = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/mn").text
        assert '外出打卡成功' == rrsult

    def test_send_massage(self):
        """
        搜索联系人欧文娟 发送信息
        :return:
        """
        sendtext = 'appium'
        # 定位到通讯录，并对它做点击操作
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击搜索框
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guu").click()
        # 搜索 欧文娟
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fk1").send_keys("欧文娟")
        # 定位到界面的欧文娟
        self.driver.find_element(MobileBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android."
                                 "widget.LinearLayout/android.widget.FrameLayout/android.widget."
                                 "RelativeLayout/android.widget.RelativeLayout/android.widget."
                                 "FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android."
                                 "widget.RelativeLayout/android.widget.RelativeLayout/android.widget."
                                 "RelativeLayout/android.view.ViewGroup/android.widget.TextView").click()
        # 定位到 发信息 点击
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/abo").click()
        # 定位到发送信息框，且输入 appium
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/dx1").send_keys("appium")
        # 点击发送
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/dwx").click()
        elements = self.driver.find_elements(MobileBy.XPATH, '//*[@text="appium"]')
        assert elements[-1].text == sendtext
