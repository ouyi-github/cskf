import pytest
from python_yuan.clac import Clac #导入待测试的代码


@pytest.mark.parametrize('step',['jia','jian','cheng','chu'])
def test_step(step):
    a = 10
    b = 20 #实际工作中，测试数据也是参数化的。这里为了方便理解，把数据写死了。
    if step == 'jia':
        result = Clac(a,b).clac_jia()
        except1 = a + b
    elif step == 'jian':
        result = Clac(a,b).clac_jian()
        except1 = a - b
    elif step == 'cheng':
        result = Clac(a,b).clac_cheng()
        except1 = a * b
    elif step == 'chu':
        result = Clac(a,b).clac_chu()
        except1 = a / b
    assert result == except1



