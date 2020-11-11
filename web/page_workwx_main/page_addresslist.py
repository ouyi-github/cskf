from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from web.page_workwx_main.page.page_base import PageBase
from web.page_workwx_main.page.page_member import AddMember


class AddressList(PageBase):
    def goto_add_member(self):
        """实现点击添加成员按钮的方法"""
        self.wait_for_click((By.CSS_SELECTOR,'.ww_operationBar .js_add_member'))
        self.find_element(By.CSS_SELECTOR,'.ww_operationBar .js_add_member').send_keys(Keys.ENTER)
        return AddMember()
