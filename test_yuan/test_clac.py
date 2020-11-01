import pytest
from python_yuan.clac import Clac

class TestClac:

    @pytest.mark.add
    @pytest.mark.parametrize("a,b,c",[(1,1,2),(-1,2,1),(-3,-8,-11)])
    def test_jia(self,a,b,c):
        result = Clac(a,b).clac_jia()
        assert result == c

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,c",[(1,1,0),(-1,2,-3),(-3,-8,5)])
    def test_jian(self,a,b,c):
        result = Clac(a, b).clac_jian()
        assert result == c

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,c", [(1, 1, 1), (-1, 2, -2), (-3, -8, 24)])
    def test_cheng(self,a,b,c):
        print("aaa")
        result = Clac(a, b).clac_cheng()
        assert result == c

    @pytest.mark.parametrize("a,b,c", [(1, 1, 1), (-1, 2, -0.5), (-3, -8, -3/-8)])
    def test_chu(self,a,b,c):
        result = Clac(a, b).clac_chu()
        assert result == c


