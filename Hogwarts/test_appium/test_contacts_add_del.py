
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


# # 创建一个方法，用来读取yml文件
def get_datas():
    with open("./datas1/contacts.yml", encoding='utf-8') as f:
        contact_datas = yaml.safe_load(f)
        addcontact = contact_datas['add']
        delcontact = contact_datas['del']
    return [addcontact, delcontact]


class TestContacts:
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

    # @pytest.mark.parametrize("name","gender","phonenum",[
    #     ["hogwarts002","女","13325288855"],
    #     ["hogwarts003", "女", "13325288856"]
    # ])

    @pytest.mark.parametrize("name,gender,phonenum", get_datas()[0])
    def test_addcontact(self, name, gender, phonenum):
        """
        添加联系人
        :return:
        """
        # name = 'hogwarts002'
        # gender = '女'
        # phonenum = '13325288855'
        # 定位到通讯录，并做点击操作
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击 添加成员，当成员很多时不会显示在第一页，需要滑动到最后
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        # 点击 手动输入添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 定位到手机，通过先定位到 姓名 的父节点再定位到下面的输入框
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        # 定位到性别
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        element = self.driver.find_element(MobileBy.XPATH, "//*[@text='男']")
        if gender == '女':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            # 加入一个显示等待
            WebDriverWait(self.driver, 10).until(element).click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # 定位到手机号码
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'手机') and @class='android.widget.TextView']/..//*[@text='手机号']") \
            .send_keys(phonenum)
        # 点击保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gur").click()
        sleep(2)
        # 打印下页面布局，看布局下有没有 toast
        # print(self.driver.page_source)
        mytoast = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").text

        assert '添加成功' == mytoast

    # @pytest.skip
    @pytest.mark.parametrize("membername", get_datas()[1])
    def test_delete_contact(self, membername):
        """
        删除成员
        :return:
        """
        # membername = 'hogwarts002'
        # 定位到通讯录，并做点击操作
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 定位到 搜索
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/guu").click()
        # 定位到搜索输入框
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(membername)
        sleep(2)
        # 判断成员是否存在，存在的话 membername文本应该为2，不存在的话那就只有一个membername(老师写的方式)
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{membername}']")
        beforenum = len(eles)
        if beforenum < 2:
            print("没有可删除人员")
            # return 不进行后面的操作
            return
        # 否则的话，继续往下走，找到第二个进行点击操作
        eles[1].click()

        #  # 确定成员是否存在（自己写的方式）
        # try:
        #     elename = self.driver.find_element(MobileBy.XPATH,
        #                                        f"//*[@text='{membername}' and @class='android.widget.TextView']").text
        #     assert membername == elename
        #     elename.click()
        # except:
        #     print("成员不存在")
        # sleep(2)
        # 进入个人信息页面
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guk']").click()
        # 点击 编辑成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        # 点击删除成员
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()
        # 点击 确定 删除
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        sleep(2)
        # 判断是否删除成功(自己写的方式)
        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{membername}']")
        afternum = len(eles1)
        assert afternum == 1

        # # 老师写的方法，判断membername个数是不是比之前少了一个
        # eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{membername}']")
        # afternum = len(eles1)
        # assert afternum == beforenum - 1
