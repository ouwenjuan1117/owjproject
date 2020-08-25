from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""
    def __init__(self , driver_base = None):
        print("1111111111111111111")
        # 避免driver 的重复实例化
        if driver_base is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver: WebDriver = driver_base

        if self._base_url != "":
            self.driver.get(self._base_url)
        self.driver.implicitly_wait(3)

    def find(self, by, value):
        return self.driver.find_element(by , value)

    def finds(self, by, value):
        return self.driver.find_elements(by, value)

    def wait_for_clickable(self, element):
        """
        显示等待元素可被点击
        :param element:
        :return:
        """
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))

    def wait(self, element):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(element))

