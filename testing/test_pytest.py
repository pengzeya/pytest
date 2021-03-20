# - * - coding : utf-8 - * -
# @Time ： 2021/3/19 17:51 
# @author ： pengzeya
# @Email ： 281232686@qq.com
import pytest

from python import calc
import sys

sys.path.append('..')

class TestCalc:
    def setup(self):
        pass
    @pytest.mark.parametrize('data1,data2,expect',[(1,2,3)])
    def test_add(self,data1,data2,expect):
        self.calc = calc.Calc()
        result1 = self.calc.add(data1, data2)
        print(result1)
        assert expect ==result1

    def test_add_1(self,data1,data2,expect):
        self.calc = calc.Calc()
        result1 = self.calc.add(data1, data2)
        print(result1)
        assert expect == result1

    def test_div(self):
        self.calc = calc.Calc()
        result2 = self.calc.div(2,2)
        assert 1 == result2

if __name__ == '__main__':
    pytest.main()

