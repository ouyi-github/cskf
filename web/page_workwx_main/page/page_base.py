from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageBase:
    _driver:WebDriver = None
    _base_url = ''

    def __init__(self,deiver:WebDriver = None):
        if self._driver is None and deiver is None:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(5)
        elif self._driver is None and deiver is not  None:
            self._driver = deiver
        else:
            self._driver.implicitly_wait(5)

        if self._base_url != '':
            self._driver.get(self._base_url)

    def find_element(self,c_method,c_value):
        # 封装单个元素查找的方法
        return self._driver.find_element(c_method,c_value)

    def find_elements(self,c_method,c_value):
        # 封装多个元素的查找方法
        return self._driver.find_elements(c_method,c_value)

    def wait_for_click(self,c_ele):
        """封装显示等待方法"""
        return WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable(c_ele))









