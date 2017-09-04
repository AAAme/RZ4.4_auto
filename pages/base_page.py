# coding=utf-8
# 所有的page继承base_page
from base.driver import TestDriver


class BasePage(object):
    def __init__(self, driver:TestDriver):
        self.base_driver = driver

    def open(self, url):
        self.base_driver.get_url(url)
        self.base_driver.max_window()

