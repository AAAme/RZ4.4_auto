# editor: liuyanghui 2017/9/1
# 创建客户操作（创建使用新的联系人与使用已有联系人）
#
#
#


from pages.main_pages.main_page import MainPage


class CustomerPage(MainPage):

    def create_custom(self, cus_data):
        """
        添加客户，注意分创建新的联系人与使用已有联系人
        :param cus_data: 字典格式，对应要填入的值
        :return: 
        """

        self.base_driver.impli_wait()
        self.base_driver.click("l, 客户")
        self.base_driver.impli_wait()
        self.base_driver.click("l,  添加客户")

        #  添加客户
        self.base_driver.impli_wait()
        self.base_driver.clear_type("i, name", cus_data["name"])
        # 是否勾选“公共”，0不勾选,1勾选
        if cus_data["public"] == "1":
            self.base_driver.click("i, public")
        elif cus_data["public"] == "0" or cus_data["public"] == '':
            pass
        else:
            print("输入的public值非法")
        # 是否选择已有联系人，0新增,1选取已有的
        if cus_data["selectContact"] == "0" or cus_data["selectContact"] == '':
            pass
            self.base_driver.clear_type("i, contact", cus_data["contact"])
            self.base_driver.clear_type("i, phone", cus_data["phone"])
            self.base_driver.clear_type("i, email", cus_data["email"])
            self.base_driver.clear_type("i, qq", cus_data["email"])
        elif cus_data["selectContact"] == "1":
            pass
            self.base_driver.click("i, selectContact")
            self.base_driver.click("i, contactID_chosen")
            self.base_driver.click("s, #contactID_chosen > div > ul > li:nth-child(1)")
        else:
            print("输入的selectContact值非法")

        self.base_driver.clear_type("i, depositor", cus_data["depositor"])  # 对公账户
        if cus_data["type"] != '':
            self.base_driver.select_by_text("i, type", cus_data["type"])  # 按照带选项名字选择
        self.base_driver.sleep(2)
        if cus_data["size"] != '':
            self.base_driver.select_by_text("i, size", cus_data["size"])
        if cus_data["status"] != '':
            self.base_driver.select_by_text("i, status", cus_data["status"])
        if cus_data["level"] != '':
            self.base_driver.select_by_text("i, level", cus_data["level"])
        self.base_driver.clear_type("n, address[title]", cus_data["addressTitle"])

        self.base_driver.clear_type("n, address[location]", cus_data["addressLocation"])
        self.base_driver.clear_type("i, intension", cus_data["intension"])

        self.base_driver.click("i, submit")  # 点击保存按钮

        # 确定创建成功并且返回客户列表成功
        # assert self.get_last_customer() == cus_data["name"]
        #
        # assert "http://localhost/ranzhi/www/crm/customer-browse.html" == self.base_driver.get_current_url()


    def get_last_customer(self):
        """
        取刚刚创建的客户的信息
        :return: 客户姓名
        """
        name = self.base_driver.get_element("s, #browseForm > table > tbody > tr:nth-child(1) > td:nth-child(2)").text
        return name






