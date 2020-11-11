from selenium import webdriver

from web.page_workwx_login.index import Index


class TestPage:
    def setup(self):
        self._driver = webdriver.Chrome()
        self.index = Index(self._driver)
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()
    def teardown(self):
        self._driver.quit()

    def test_page1(self):
        """首页点击立即注册》注册页注册"""
        self.index.goto_register().register()

    def test_page2(self):
        """首页点击企业登录》登录页点击立即注册》注册页注册"""
        self.index.goto_login().goto_register().register()
