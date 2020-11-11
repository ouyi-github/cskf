from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from web.page_workwx_main.page.page_base import PageBase
from web.page_workwx_main.page.page_member import AddMember
from web.page_workwx_main.page_addresslist import AddressList


class Main(PageBase):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_member(self):
        """实现点击添加成员按钮的方法"""
        self.wait_for_click((By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)'))
        self._driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').send_keys(Keys.ENTER)
        print('点击添加按钮')
        return AddMember()

    def goto_address_list(self):
        """实现点击通讯录按钮的方法"""
        self.wait_for_click((By.ID,'menu_contacts'))
        self._driver.execute_script('document.getElementById("menu_contacts").click()')
        return AddressList()




