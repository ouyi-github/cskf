
from selenium import webdriver
from selenium.webdriver import ActionChains,TouchActions
import pytest
from time import sleep
from selenium.webdriver.common.keys import Keys
import os

class TestBroswer:
    def setup(self):

        # 获取执行测试用例时传入的broswer的值，来判断使用哪个浏览器
        broswer = os.getenv('broswer')
        if broswer == 'firefox':
            self.driver = webdriver.Firefox()
        elif broswer == 'chrome':
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()  # 最大化窗口

    def teardown(self):
        self.driver.quit()

    def test_broswer(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)



















