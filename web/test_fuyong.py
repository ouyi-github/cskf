from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class Testbroswer:
    def setup(self):
        option = Options() #创建一个option对象
        option.debugger_address = '127.0.0.1:9222' #option使用指定的浏览器程序
        self.driver = webdriver.Chrome(options=option) #使用指定的option生成driver
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_broswer(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame") #此时进入企业微信网页时，就已经是登录状态了
        print(self.driver.get_cookies())
        self.driver.find_element_by_id('menu_contacts').click() #点击通讯录按钮
        sleep(10)
