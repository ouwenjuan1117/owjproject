from Hogwarts.test_selenium.test_project.pages.main_page import MainPage


if __name__ == '__main__':


    main = MainPage()

    # 1.从首页跳转到添加成员页面  2.添加成员页面  3.点击保存
    # self.main.go_to_add_member().add_member().save_member()
    main.go_to_add_member().add_member()