# - * - coding : utf-8 - * -
# @Time ： 2021/3/21 17:07 
# @author ： pengzeya
# @Email ： 281232686@qq.com
from time import sleep

import selenium
from selenium import webdriver

class TestYueguang():
    def setup(self):
        self.driver =webdriver.Chrome()
        self.driver.get('http://182.254.188.244/')
        self.driver.maximize_window()
        self.driver.implicitly_wait('5')
    def teardown(self):
        self.driver.quit()

    def test_yueguang(self):
        self.driver.find_element_by_name('wd').send_keys('女神')
        sleep(2)
        self.driver.find_element_by_link_text('搜索').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="txt"]').send_keys('杨导')
        sleep(2)
        self.driver.find_element_by_link_text('搜索').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[1]/div[2]/h4/a').click()
        sleep(6)
        self.driver.find_element_by_id('user_name').send_keys('281232686')
        sleep(2)
        self.driver.find_element_by_id('user_pwd').send_keys('user_pwd')
        sleep(2)
        self.driver.find_element_by_id('btn_submit').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="uindex"]/div[1]/div/ul/li[1]/a').click()
