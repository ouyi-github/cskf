class Clac:
    """创建加减乘除类"""

    def __init__(self,a,b):
        """获取数据"""
        self.a = a
        self.b = b

    def clac_jia(self):
        """加法计算方法"""
        return self.a + self.b

    def clac_jian(self):
        return self.a - self.b

    def clac_cheng(self):
        return self.a * self.b

    def clac_chu(self):
        return self.a / self.b


