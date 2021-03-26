# - * - coding : utf-8 - * -
# @Time ： 2021/3/23 18:30 
# @author ： pengzeya
# @Email ： 281232686@qq.com
from appium import webdriver
desired_caps ={}
#系统
desired_caps['platformName'] = 'Android'

desired_caps['platformVersion']  = '10'

desired_caps['deviceName'] = 'efe8a802'

desired_caps['appPackage'] ='com.ss.android.ugc.aweme'

desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.splash.SplashActivity'
# desired_caps
driver = webdriver.Remote('http://0.0.0.1:4723/wb/hub',desired_caps)
