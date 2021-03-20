# - * - coding : utf-8 - * -
# @Time ： 2021/3/20 23:47 
# @author ： pengzeya
# @Email ： 281232686@qq.com

class TestDemo:
    def setup_class(self):
        #第一步 打开浏览器
        print('setup_class,第一步 打开浏览器')
    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def teardown_class(self):
        print('eardown_class,第五步 关闭浏览器')

    def test_a(self):
        print('testa')

    def test_b(self):
        print('testb')

    def test_c(self):
        print('testc')