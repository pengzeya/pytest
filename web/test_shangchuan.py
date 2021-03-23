# - * - coding : utf-8 - * -
# @Time ： 2021/3/22 19:45 
# @author ： pengzeya
# @Email ： 281232686@qq.com
from time import sleep

from selenium import webdriver

class TestFile():
    def setup(self):
            self.driver = webdriver.Chrome()
            self.driver.get('http://image.baidu.com')
            self.driver.maximize_window()
            self.driver.implicitly_wait('5')

    def teardown(self):
        self.driver.quit()

    def test_file(self):
        self.driver.get('http://image.baidu.com')
        self.driver.maximize_window(10)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_xpath('//*[@id="uploadImg"]').send_keys('‪C:\Users\28123\Desktop\微信图片_20201212163532.jpg')
        sleep(3)
