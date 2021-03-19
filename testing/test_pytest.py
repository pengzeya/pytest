# - * - coding : utf-8 - * -
# @Time ： 2021/3/19 17:51 
# @author ： pengzeya
# @Email ： 281232686@qq.com
import pytest

from python import calc


class TestCalc:
    def setup(self):
        pass
    def test_add(self):
        self.calc = calc.Calc()
        result1 = self.calc.add(1, 2)
        print(result1)

    def test_div(self):
        self.calc = calc.Calc()
        result2 = self.calc.div(2,2)
        assert 1 == result2

if __name__ == '__main__':
    pytest.main()
