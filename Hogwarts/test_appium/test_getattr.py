from appium import webdriver
from hamcrest import *


class TestGetAttr():

    def setup(self):
        desire_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
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

    # 把整条用例设置成跳过
    # @pytest.mark.skip
    def test_get_attr(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # 获取content-desc的属性
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        # 设置普通断言,search在search_ele.get_attribute("resource-id")这个属性当中
        assert 'search' in search_ele.get_attribute("resource-id")

    def test_hamcrest(self):
        assert_that(10, equal_to(10), '这是一个提示信息')
        # 10是对比的值，2是跟着的浮动范围
        assert_that(8, close_to(10, 2))
        # 前面字符串包含后面的字符串的
        assert_that('contains some string', contains_string('string'))
