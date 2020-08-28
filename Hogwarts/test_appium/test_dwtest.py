import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDw():

    def setup(self):
        desire_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            # 不要停止被测应用程序的进程
            # "dontStopAppOnReset":"True",
            # 跳过设备初始化，包括：安装和运行“设置”应用或权限设置，可用于提高启动性能
            "skipDeviceInitialization": "true",
            # 启用Unicode输入，设置执行用例时的编码为中文
            "unicodeKeyboard": "true",
            # 在运行具有unicodeKeyboard功能的Unicode测试之后，将键盘重置为其原始状态
            "resetKeyboard": "true",
            # 在此会话之前，请勿重置应用程序状态
            "noReset": True
        }
        # 127.0.0.1:4723是启动appium server服务的地址      /wd/hub 是固定写法   desire_caps是要告诉server一些信息，需要测试的平台、设备、包等
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        # 建立连接以后，模拟器有点慢，加一个隐示等待
        self.driver.implicitly_wait(20)

    def teardown(self):
        # # 返回上一步操作
        # self.driver.back()
        self.driver.quit()

    def test_search(self):
        print("雪球主页面搜索测试用例")
        """
        1.打开雪球APP
        2.点击搜索输入框
        3.向搜索输入框里面输入‘阿里巴巴’
        4。在搜索结果里面选择‘阿里巴巴’，然后进行点击
        5.获取这只阿里巴巴的股价，并判断这个股价的价格，大于200
        """
        # 定位到搜索框
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        # 输入阿里巴巴
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")
        # 定位到联想出来的第一个阿里巴巴
        el3 = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        el3.click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200

    # 元素属性的判断
    def test_attr(self):
        """
        1.打开雪球APP
        2.定位首页的搜索框
        3.判断搜索框是否可用，并查看搜索框name的属性
        4.打印搜索框这个元素的左上角坐标和它的宽度
        5.向搜索框输入：alibab
        6.判断阿里巴巴是否可见
        7、如果可见，打印 搜索成功，如果不可见，打印 搜索失败
        :return:
        """
        # 判断搜索框是否可用
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(element.is_enabled())
        # 如果搜索框可用，对它进行点击
        search_enabled = element.is_enabled()
        # 获取元素的文本信息
        print(element.text)
        # 打印它的元素坐标
        print(element.location)
        # 打印它的宽和高
        print(element.size)
        if search_enabled == True:
            element.click()
            # 输入阿里巴巴
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            # 定位到第一个阿里巴巴
            alibaba_element = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # 获取displayed属性
            print(alibaba_element.get_attribute("displayed"))
            element_displayed = alibaba_element.get_attribute("displayed")
            if element_displayed == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        action = TouchAction(self.driver)
        # 获取当前屏幕的尺寸
        print(self.driver.get_window_rect())  # {'width': 720, 'height': 1280, 'x': 0, 'y': 0}
        window_rect = self.driver.get_window_rect()
        width = window_rect["width"]
        height = window_rect["height"]
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        # 因为坐标容易改变，所以不甜建议用这种方法
        # action.press(x=349,y=415).wait(200).move_to(x=349,y=516).release().perform()
        time.sleep(15)
        action.press(x=x1, y=y_start).wait(1000).move_to(x=x1, y=y_end).release().perform()
