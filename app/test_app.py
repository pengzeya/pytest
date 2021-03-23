# - * - coding : utf-8 - * -
# @Time ： 2021/3/23 18:30 
# @author ： pengzeya
# @Email ： 281232686@qq.com
from appium import  webdriver
driver = webdriver.Remote('http://127.0.0.1:4723/wb/hub',desired_capabilities=desired_caps)
