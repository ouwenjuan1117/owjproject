import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestBrowser():

    def setup_method(self, method):
        # 复用浏览器时，需要先命令行启动，之后添加一个debugger地址
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        # 初始化环境，调用浏览器
        self.driver = webdriver.Chrome()
        # 最大化窗口
        self.driver.maximize_window()
        # 隐示等待，当我们进入一个页面时会动态的等到5秒，找到以后就立刻执行，没找到就继续等到5秒
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        # 最后退出
        self.driver.quit()

    def test_cookie(self):
        # 打开index页面，这时候需要登录，第一次打开页面时没有登录cookie，无法登录成功
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # cookie信息经常过期，等待10秒，然后手动扫码登录，之后把cookie信息，存入数据库
        sleep(10)

        # shelve是Python内置的模块 可提供的小型数据库问
        # get_cookie()可以用来获取当前页面的cookies,获取当扫码之后的cookies信息，先把获取到的数据，存在cookies文件夹
        # cookies = self.driver.get_cookies()
        db = shelve.open('./mydbs/cookies')
        # 创建一个key用来存取cookies
        # db['cookie']=cookies
        # db.close()

        # 把数据从数据库取出来
        cookies = db['cookie']

        # print(cookies)
        # 带有登录信息的cookies，通过self.driver.get拿到的
        # cookies =[{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'VhrR91WDroKVULbioa9KoDeMyaTd8c_to7loaIaevbn0Gc2Oi5DHZRRsUxkF8A3AcspyafRM1XCp-7oJp9J8Wws1aq0DASlwfMev8SYOwnhLWEsQnbRihB9taI_lKKqZIApj2HkG_TYPvWyP3XO9rKr93Mx6TY72FxyJr_zTq7HymC45SEMJgplKdqZmMigSTZGtfmB4l7BsgmqrWWBCIJDxB22erKPSJrjXvxXs29X_8lpV68r3I8ZHz19Afjvx-OcWlWb6t_K4a8Wqt-peQg'},
        #           {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853798781085'},
        #           {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'},
        #           {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'CXfZ39t3ljpke0eZrrTHC8ncCPCdrkXzP2cnkM4Vrx21KjvuRW_68gYku04Jg-6S'},
        #           {'domain': '.work.weixin.qq.com', 'expiry': 1629439356, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597903346,1597903356'},
        #           {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6585504'},
        #           {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '13552546471007720'},
        #           {'domain': '.qq.com', 'expiry': 1660979819, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1355958772.1597903346'},
        #           {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853798781085'},
        #           {'domain': '.work.weixin.qq.com', 'expiry': 1629439333, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},
        #           {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'},
        #           {'domain': 'work.weixin.qq.com', 'expiry': 1597934869, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '62k4eu2'},
        #           {'domain': '.qq.com', 'expiry': 1597994219, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.462806736.1597903346'},
        #           {'domain': '.work.weixin.qq.com', 'expiry': 1600499822, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'},
        #           {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325105153580'},
        #           {'domain': '.qq.com', 'expiry': 1906005064, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_5ecf514a4005f'},
        #           {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '3135559060'}]

        for cookie in cookies:
            # 当时间戳如果是浮点数时，有可能会报错，可以直接删除
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            # add_cookie()可以往当前页面上添加一些cookie信息，添加的是一个字典类型（不支持浮点数）
            self.driver.add_cookie(cookie)
        # 给一个cookie之后进行二次登录，有了cookie之后登录成功
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        self.driver.find_element_by_xpath('//*[@id="js_upload_file_input"]').send_keys(
            r'C:\Users\ouwenjuan\Desktop\新成员表.xlsx')
        assert '新成员表.xlsx' == self.driver.find_element_by_id('upload_file_name').text
        sleep(3)
