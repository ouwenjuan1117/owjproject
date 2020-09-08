import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy

from Hogwarts.test_appium.pages.app import App


# # 创建一个方法，用来读取yml文件
def get_datas():
    with open("./datas1/contacts.yml", encoding='utf-8') as f:
        contact_datas = yaml.safe_load(f)
        addcontact = contact_datas['add']
        delcontact = contact_datas['del']
    return [addcontact, delcontact]

class TestAddContact:

    def setup(self):
        """
        应用的启动
        :return:
        """
        # 实例化一个APP，帮我们启动应用
        self.app = App()
        # 通过start()方法里的 return self之后调用goto_main()  跳转到首页
        self.main = self.app.start().goto_main()

    def teardown(self):
        """
        应用的关闭
        :return:
        """
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phonenum", get_datas()[0])
    def test_addcontact(self, name, gender, phonenum):
        """
        通过self.main方法主页面调用goto_addresslist()进入到通讯录，通过通讯录调用add_member()之后进入添加成员页面，调用手动添加输入addcontact_menual()
        之后输入姓名、性别、电话号码，点击保存，断言是否成功
        :return:
        把页面存为mypage
        """
        # name = 'hogwarts005'
        # gender = '女'
        # phonenum = '13325288855'
        mypage = self.main.goto_addresslist().add_member().addcontact_menual(). \
            edit_name(name).edit_gender(gender).edit_phonenum(phonenum).click_save()
        mytosat = mypage.goto_tosat()
        assert "添加成功" == mytosat

    @pytest.mark.parametrize("membername", get_datas()[1])
    def test_delcontact(self, membername):
        # membername = "hogwarts003"
        delpage = self.main.goto_addresslist().goto_click_search().search_sendkeys(membername). \
            search_sendkeys_click(membername).click_more().edit_member().del_member(membername)
        afternum = delpage.goto_determine_del(membername)
        assert afternum == 1
