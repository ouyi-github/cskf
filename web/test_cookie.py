from selenium import webdriver
from time import sleep


class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # 将cookies放入变量中
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850814799304'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 't9WeHiLQAywSBmGmI12gOsE0ilqI3OJIxMS66KYmvznSI4VRY3ZxzJbFifXMg5f_QmSTOcfJ-1CesO3czeqYLiBwe7PMQttF54rA2hSBCXMNbVnb42PLJOco1ntRxj2f927lX2RRoj4sPH0gkB7QKglF-4TAAwwWXOSDXHx2j4Z7cS0yjmikvvsvb0E50u99c9t0zHJJ4AC9rsufkv-YWn_Zp7PGiLFeSP1upcN2xOSw2vP_lgJ4p4LtHvRMJK6nEXMJkliTZ7a8qwRROS8r2w'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850814799304'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325100191509'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636300223, 'httpOnly': False,
                                            'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
                                            'secure': False, 'value': '1604758667,1604758842,1604764224'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a8686426'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'XpgcPt60DeBa2-FcophxYISeXtHo4nMqsljZ5C7mKq1OfUBAg0klxY7ixrRkKe2m'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '2298449271234700'},
            {'domain': '.qq.com', 'expiry': 1604851539, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1592559454.1604758667'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604790194, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '1iqo9pj'},
            {'domain': '.qq.com', 'expiry': 1667837139, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1580179371.1604758667'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636294658, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607357565, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts") #第一次打开网页
        # 传入cookie
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts") #再次打开网页，此时变为了登录状态
        sleep(5)