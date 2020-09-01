import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestParam():

    def setup(self):
        desire_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            # "dontStopAppOnReset":"True",
            "skipDeviceInitialization": "true",
            "unicodeKeyboard": "true",
            "resetKeyboard": "true",
            # 在此会话之前，请勿重置应用程序状态
            "noReset": 'true'
        }
        # 127.0.0.1:4723是启动appium server服务的地址      /wd/hub 是固定写法   desire_caps是要告诉server一些信息，需要测试的平台、设备、包等
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        # 建立连接以后，模拟器有点慢，加一个隐示等待
        self.driver.implicitly_wait(20)

    def teardown(self):
        # 执行完之后点击取消，返回搜索框
        self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
        # 返回上一步操作
        # self.driver.back()
        # self.driver.quit()

    # 把整条用例设置成跳过
    # @pytest.mark.skip
    @pytest.mark.parametrize("searchkey,type,expect_price", [("alibaba", 'BABA', 288), ("小米", "01810", 26)])
    def test_search(self, searchkey, type, expect_price):
        """
        1、打开雪球
        2、点击搜索框
        3、输入搜索词（阿里巴巴，小米）
        4、点击第一个搜索结果
        5、判断股票价格
        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()
        # 通过找到BABA的层级关系定位到当前的价格的属性
        price_element = self.driver.find_element(MobileBy.XPATH,
                                                 f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # 拿到当前价格
        current_price = float(price_element.text)
        # 设置期望的价格
        # expect_price =180
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))
