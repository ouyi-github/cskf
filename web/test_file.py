from time import sleep
from selenium import webdriver
class Test_File:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_file(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="form"]/span[1]/span[1]').click() #点击按图片搜索按钮
        ele = self.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input') #定位到上传文件按钮
        ele.send_keys('/home/ouyi/goods02.jpg') #上传图片
        sleep(3)