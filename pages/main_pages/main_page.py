# editor：liuyanghui  data:2017/9/1
# 系统登录后的第一个页面
#
#
#
from pages.login_page.login_page import LoginPage


class MainPage(LoginPage):

    # 登出
    def logout(self):
        self.base_driver.impli_wait()
        self.base_driver.switch_default_frame()
        self.base_driver.click("i, start")
        self.base_driver.impli_wait()
        self.base_driver.click("l,  退出")
        self.base_driver.sleep(2)
        self.base_driver.close_browser()

    # 进入指定的模块
    def enter_app(self, index):
        """
        
        :param index: 1:我的地盘 2：客户管理 3：日常办公 4：项目 5：文档
                        6：现金记账 7：团队
        :return: none
        """
        if index == "1":
            self.base_driver.switch_default_frame()
            self.base_driver.click("i, s-menu-dashboard")
        elif index == "2":
            self.base_driver.switch_default_frame()
            self.base_driver.click("i, s-menu-1")
            self.base_driver.switch_frame("i, iframe-1")
        elif index == "3":
            self.base_driver.switch_default_frame()
            self.base_driver.click("i,  s-menu-2")
            self.base_driver.switch_frame("i, iframe-2")
        elif index == "4":
            self.base_driver.switch_default_frame()
            self.base_driver.click("i,  s-menu-3")
            self.base_driver.switch_frame("i, iframe-3")
        elif index == "5":
            self.base_driver.switch_default_frame()
            self.base_driver.click("i,  s-menu-4")
            self.base_driver.switch_frame("i, iframe-4")
        elif index == "6":
            self.base_driver.switch_default_frame()
            self.base_driver.click("i,  s-menu-5")
            self.base_driver.switch_frame("i, iframe-5")
        elif index == "7":
            self.base_driver.switch_default_frame()
            self.base_driver.click("i,  s-menu-6")
            self.base_driver.switch_frame("i, iframe-6")
        else:
            print("传入的值非法，应为1-7")
