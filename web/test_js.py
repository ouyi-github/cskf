
from selenium import webdriver
from time import sleep
class TestJs:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_js(self):
        self.driver.get("https://www.12306.cn/index/")
        # 使用selenium执行js脚本
        # 定位到时间控件元素,并移除时间控件的readonly属性
        self.driver.execute_script('a = document.getElementById("train_date");a.removeAttribute("readonly")')
        self.driver.execute_script('a.value="2020-12-22"') #给时间控件的value赋值
        sleep(3)

        


