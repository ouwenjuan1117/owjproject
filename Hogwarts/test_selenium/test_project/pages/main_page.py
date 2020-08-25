from selenium.webdriver.common.by import By

from Hogwarts.test_selenium.test_project.pages.add_member_page import  AddMemberPage
from Hogwarts.test_selenium.test_project.pages.basepage import BasePage
from Hogwarts.test_selenium.test_project.pages.contact_page import ContactPage


class MainPage(BasePage):
    '''点击通讯录'''
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    def go_to_contact(self):
        # 对 contactpage 类进行实例化,表示业务逻辑的转换关系
        self.find(By.CSS_SELECTOR, "[id='menu_contacts']").click()
        return ContactPage(self.driver)

    def go_to_add_member(self):
        '''点击添加成员'''
        self.find(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        # 对addmemberpage 类进行实例化,表示业务逻辑的转换关系
        # 第二次实例化，子类AddMemberPage 初始化，子类在初始化的时候会调用父类的init函数，这时候self.driver已经是有值的，所以直接走的else
        return AddMemberPage(self.driver)

# 用作调试self.driver
# if __name__ == '__main__':
#     main = MainPage()
#     main.go_to_add_member().add_member().save_member()
