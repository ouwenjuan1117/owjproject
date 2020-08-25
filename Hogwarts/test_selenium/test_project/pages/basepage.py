
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ''

    def __init__(self, driver=None):
        # 实现避免driver的重复实例化
        if driver is None:
            # 复用浏览器时，需要先命令行启动，之后添加一个debugger地址
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)

        else:
            # 加一个注解，WebDriver，是为了在别的时候用driver进行类型提示
            self.driver: WebDriver = driver
        # BasePage只提供公共方法，和业务相关的应该单独放开，所以URL不应该放在这里
        if self.base_url != '':
            self.driver.get(self.base_url)

        # 找不到元素时，加一个隐示等待
        self.driver.implicitly_wait(3)

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        return self.driver.find_elements(by, value)

    def wait_for_clickable(self, element):
        """
        显式等待元素可被点击
        :param element:
        :return:
        """

        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))

    def wait(self, element):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(element))

    def go_to_main_page(self):
        return self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
