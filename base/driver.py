#
# 封装的selenium方法页面
#
#

import csv
import string
from time import sleep

import pymysql
from selenium import webdriver
from selenium.webdriver.support.select import Select


class TestDriver(object):
    def __init__(self, browser):
        """
        
        :param browser: 
        :usage:
            
        """
        if browser == "Chrome" or "chrome":
            try:
                driver = webdriver.Chrome()
                self.driver = driver
            except:
                print("chrome error")
        elif browser == "Firefox" or "firefox":
            try:
                driver = webdriver.Firefox()
                self.driver = driver
            except:
                print("firefox error")
        else:
            print("no browser error")

    def get_element(self,
        selector):
        selector_by = selector.split(",")[0].strip()
        selector_value = selector.split(",")[1].strip()

        if selector_by == "i":
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == "n":
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c":
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l":
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "s":
            element = self.driver.find_element_by_css_selector(selector_value)
        elif selector_by == "x":
            element = self.driver.find_element_by_xpath(selector_value)
        elif selector_by == "t":
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "p":
            element = self.driver.find_element_by_partial_link_text(selector_value)
        else:
            raise NameError("no valid selector comes")
        return element

    def get_elements(self, selector: string):

        selector_by = selector.split(",")[0].strip()
        selector_value = selector.split(",")[1].strip()
        try:
            if selector_by == "i":
                elements = self.driver.find_elements_by_id(selector_value)
            elif selector_by == "n":
                elements = self.driver.find_elements_by_name(selector_value)
            elif selector_by == "c":
                elements = self.driver.find_elements_by_class_name(selector_value)
            elif selector_by == "l":
                elements = self.driver.find_elements_by_link_text(selector_value)
            elif selector_by == "s":
                elements = self.driver.find_elements_by_css_selector(selector_value)
            elif selector_by == "x":
                elements = self.driver.find_elements_by_xpath(selector_value)
            elif selector_by == "t":
                elements = self.driver.find_elements_by_tag_name(selector_value)
            elif selector_by == "p":
                elements = self.driver.find_elements_by_partial_link_text(selector_value)
            else:
                raise NameError("get_elements error")
            return elements
        except:
            print("get_elements error")

    def click(self, selector):
        ele = self.get_element(selector)
        ele.click()

    def type(self, selector, text):
        ele = self.get_element(selector)
        ele.send_keys(text)

    def clear_type(self, selector, text):
        try:
            ele = self.get_element(selector)
            ele.clear()
            ele.send_keys(text)
        except:
            print("clear_type error")

    def get_url(self, url):
        try:
            self.driver.get(url)
        except:
            print("get_url error")

    def impli_wait(self, time=20):
        try:
            self.driver.implicitly_wait(time)
        except:
            print("impli_wait error,time=%s" % time)

    def max_window(self):
        try:
            self.driver.maximize_window()
        except:
            print("max_window error")

    def switch_default_frame(self):  # 转换到最外层frame
        try:
            self.driver.switch_to_default_content()
        except:
            print("switch_default_frame error")

    def switch_frame(self, selector):
        try:
            ele = self.get_element(selector)
            self.driver.switch_to_frame(ele)
        except:
            print("switch_frame error")

    def switch_frames(self, selector, num):
        ele = self.get_elements(selector)
        self.driver.switch_to_frame(ele[num])

    def switch_parent_frame(self):
        try:
            self.driver.switch_to.parent_frame()
        except:
            print("switch_parent_frame error")

    def sleep(self, time):
        sleep(time)

    def select_by_text(self, selector, text):

        ele = self.get_element(selector)
        Select(ele).select_by_visible_text(text)


    def select_by_value(self, selector, value):
        try:
            ele = self.get_element(selector)
            Select(ele).select_by_value(value)
        except:
            print("select_by_value error")

    def select_by_index(self, selector, index):
        try:
            ele = self.get_element(selector)
            Select(ele).select_by_index(index)
        except:
            print("select_by_index error")

    def close_browser(self):  # 关闭当前窗口
        self.driver.close()

    def quit_browser(self):  # 关闭当前浏览器
        self.driver.quit()

    def read_csv_data(self, file_path, mode="r", encoding="utf-8"):
        self.csv_file = open(file_path, mode=mode, encoding=encoding)
        csv_data = csv.reader(self.csv_file)
        return csv_data

    def close_csv_file(self):
        self.csv_file.close()

    def read_sql_file(self, sql_filepath, mode="r", encoding="utf8", host="localhost", user="root",
                      passwd="", db="ranzhi", port=3306, charset="utf8"):
        sql_file = open(sql_filepath, mode=mode, encoding=encoding)
        sql_script = sql_file.read()
        mysql_connect = pymysql.connect(host=host, user=user,
                                        passwd=passwd, db=db, port=port, charset=charset)
        mysql_cursor = mysql_connect.cursor()
        mysql_cursor.execute(sql_script)
        mysql_data = mysql_cursor.fetchall()

        mysql_cursor.close()
        mysql_connect.close()
        sql_file.close()
        return mysql_data

    def get_current_url(self):
        return self.driver.current_url

    def get_current_title(self):
        return self.driver.title