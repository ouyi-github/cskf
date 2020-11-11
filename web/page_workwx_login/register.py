from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self,driver:WebDriver):
        self._driver = driver

    def register(self):
        """实现form表单的注册功能方法"""
        # 输入和点击等操作细节，这里我们就不写太具体。只完成两个操作示例即可
        # 数据本来应该使用参数的方式来实现，这里直接写死
        self._driver.find_element_by_id('corp_name').send_keys('华为技术有限公司') #输入公司
        self._driver.find_element_by_id('manager_name').send_keys('欧毅') #输入管理员姓名
        sleep(5)
        return True #这里应该返回注册完成后的页面
