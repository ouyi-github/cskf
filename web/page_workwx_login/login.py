from selenium.webdriver.remote.webdriver import WebDriver

from web.page_workwx_login.register import Register


class Login:
    """企业登录页面的pageObject类"""
    def __init__(self,driver:WebDriver): #driver:WebDriver，指定参数driver的类型为WebDriver，
        # 这样在使用时可以出现相关的方法提示
        self._driver = driver #将之前pageObject类中的driver复用到这个pageObject中

    def scan_login(self):
        """扫码登录的方法"""
        pass #这个方法不好实现，所有不写
    def goto_register(self):
        """实现点击立即注册按钮的方法"""
        self._driver.find_element_by_class_name('login_registerBar_link').click() #点击立即注册
        return Register(self._driver) ##返回立即注册页面的pageObject类,并且将这个driver传递给Register类
