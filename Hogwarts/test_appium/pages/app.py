"""
用来存放app端特有的操作
比如：启动应用，关闭应用，重启应用，进入到首页
"""
from Hogwarts.test_appium.pages.main_page import MainPage


class App():
    def start(self):
        """
        启动应用
        :return:
        """
        return self

    def restaet(self):
        """
        重启应用
        :return:
        """
        pass

    def stop(self):
        """
        关闭应用
        :return:
        """
        pass

    def goto_main(self) -> MainPage:
        """
        进入到主页
        :return:返回到主页面
        """
        return MainPage()
