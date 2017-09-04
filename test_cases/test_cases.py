# coding = utf-8
# 测试用例
import unittest

from base.driver import TestDriver
from pages.main_pages.crm_pages.customer_page import CustomerPage


class TestCases(unittest.TestCase):
    def setUp(self):
        pass
        self.driver = TestDriver("Chrome")
        self.customer_page = CustomerPage(self.driver)

    def test_001(self):
        self.customer_page.open("http://localhost/ranzhi/www")
        self.customer_page.login()
        self.customer_page.enter_app("2")
        pass
        csv_data = self.driver.read_csv_data(r"C:\Users\hasee\PycharmProjects\test\data\custom_data.csv")
        header = True
        for row in csv_data:
            if header:
                header = False
                continue
            data = {
                "name": row[0], "public": row[1], "selectContact": row[2], "contact": row[3], "phone": row[4],
                "email": row[5], "qq": row[6], "depositor": row[7], "type": row[8], "size": row[9],
                "status": row[10], "level": row[11], "addressTitle": row[12], "addressLocation": row[13],
                "intension": row[14]
            }
            self.customer_page.create_custom(data)

            #  做断言
            self.driver.impli_wait()
            self.driver.sleep(2)
            self.assertEqual(self.driver.get_current_url(),
                             "http://localhost/ranzhi/www/crm/customer-browse.html", "url不同，没有回到客户页面")

            self.assertEqual(self.customer_page.get_last_customer(), data["name"], "姓名不同，新建客户失败")

    def tearDown(self):
        pass
        self.driver.close_csv_file()
        # 执行清除数据的sql语句
        # self.driver.read_sql_file(r"C:\Users\hasee\PycharmProjects\test\data\delete_crm_customer.sql")
        print("清除数据")
        self.customer_page.logout()
        print("im teardowm")


if __name__ == "__main__":
    unittest.main()
