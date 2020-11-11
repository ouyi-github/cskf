from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from web.page_workwx_main.page.page_base import PageBase


class AddMember(PageBase):

    def addmember_true(self,username,id,phone):
        """实现成功添加成员的操作"""
        self.wait_for_click((By.ID,'username'))
        self.find_element(By.ID,'username').send_keys(username) #姓名
        self.find_element(By.ID,'memberAdd_acctid').send_keys(id) #账号
        self.find_element(By.ID,'memberAdd_phone').send_keys(phone) #手机
        self.find_element(By.CSS_SELECTOR,'.js_btn_save').send_keys(Keys.ENTER) #保存

    def getmember(self,value):
        self.wait_for_click((By.CSS_SELECTOR,'.ww_checkbox'))

        while True:
            list = []
            content: str = self.find_element(By.CSS_SELECTOR, '.ww_pageNav_info_text').text  # 获取1/10
            now_page, total_page = content.split('/', 1)
            eles = self.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
            list = [ele.get_attribute('title') for ele in eles]
            if value in list:
                return  True
            if int(now_page) == int(total_page):
                return False
            self._driver.execute_script('document.getElementsByClassName("ww_commonImg_PageNavArrowRightNormal")[0].click()') #翻页

