from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

class TestAlert:
    """
    打开网页：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
    将frame页面的元素1拖拽到元素2
    这时会有一个alert弹窗，操作接受alert弹窗
    点击界面的运行按钮
    """

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_alter(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame') #打开网页
        sleep(5)

