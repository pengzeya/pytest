# - * - coding : utf-8 - * -
# @Time ： 2021/3/19 17:28
# @author ： pengzeya
# @Email ： 281232686@qq.com

import unittest

from python import calc


class TestCalc(unittest.TestCase):
    def test_add_1(self):
        self.calc = calc.Calc()
        result = self.calc.add(1,2)
        print(result)
        self.assertEqual(3,result)

if __name__ == '__main__':
    unittest.main()
