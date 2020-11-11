from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.debugger_address = '127.0.0.1:9222'
driver = webdriver.Chrome(options=options)

driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
sleep(2)
# driver.find_element_by_xpath('//a[@id="menu_index"]/span').click()
# driver.execute_script('document.getElementsByClassName("index_service_cnt_itemWrap")[0].click()')
# driver.find_element_by_css_selector('.ww_operationBar .js_add_member').send_keys(Keys.ENTER)
# driver.find_element_by_css_selector('.ww_commonImg_PageNavArrowRightNormal').send_keys(Keys.ENTER)
driver.execute_script('document.getElementsByClassName("ww_commonImg_PageNavArrowRightNormal")[0].click()')
sleep(2)
