# coding=utf-8
# 前置页面-->登录ranzhi，点击crm与创建客户按钮
from base.driver import TestDriver
from pages.base_page import BasePage



class LoginPage(BasePage):

    USERNAME = "n, account"
    PASSWORD = "n, password"
    SUBMIT = "i, submit"
    KEEPLOGIN = "i, keepLoginon"

    def login(self, account="admin", password="123456", keeplog=0):  # 登录
        """      
        :param account: 账号
        :param password: 密码
        : 默认管理员登录
        :param keeplog: 是否勾选保持登录按钮，0否1是，默认0
        :return: 
        """
        self.base_driver.impli_wait()
        self.base_driver.clear_type(self.USERNAME, account)
        self.base_driver.clear_type(self.PASSWORD, password)
        if keeplog == 1:
            self.base_driver.click(self.KEEPLOGIN)
        elif keeplog == 0:
            pass
        else:
            print("输入keeplogin的值非法")
        self.base_driver.click(self.SUBMIT)

if __name__ == "__main__":
    def foo(num):
        if isinstance(num, int):
            if num<0:
                print("invaild parmer")
            elif num == 0:
                return 1
            else:
                return foo(num-1)*num
        else:
            print("invaild parmer")

    def feb(num):
        list = [1, 1]
        if isinstance(num, int):
            if num<=0:
                print("invaild parmer")
            elif num>2:
                for i in range(num-2):
                    list.append(list[i]+list[i+1])
            elif num==1:
                list=[1]
        else:
            print("error")

        print(list)

    print(foo(4))
    feb(3)







