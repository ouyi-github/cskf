from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from web.page_workwx_login.login import Login
from web.page_workwx_login.register import Register
class Index:
    """企业微信首页pageObject"""
    def __init__(self,driver:WebDriver): #driver:WebDriver，指定参数driver的类型为WebDriver，
        # 这样在使用时可以出现相关的方法提示
        self._driver = driver

    def goto_register(self):
        """点击立即注册按钮的方法"""
        self._driver.get("https://work.weixin.qq.com/")
        self._driver.find_element_by_class_name('index_head_info_pCDownloadBtn').click() #点击立即注册
        return Register(self._driver) #返回立即注册页面的pageObject类,并且将这个driver传递给Register类

    def goto_login(self):
        """点击企业登录按钮的方法"""
        self._driver.get("https://work.weixin.qq.com/")
        self._driver.find_element_by_class_name('index_top_operation_loginBtn').click() #点击企业登录
        return Login(self._driver) #返回企业登录页面的pageObject类，并且将这个driver传递给Login类
