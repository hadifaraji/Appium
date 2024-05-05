from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random

firefox_profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox()
driver.get("https://flytoday.ir")
#source = driver.find_element(By.XPATH,"//*[text()='مبدا']")
#source.click()
#test = driver.find_elements(By.XPATH,"//*[@class='option_title__BYCIp']")
#x = (random.choice(test))
#x.click()
#sleep(5)

a = driver.find_element(By.XPATH,"//*[text()='تاریخ رفت']")
a.click()
nums=["16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
x = (random.choice(nums))
date = "//*[@class='day_dayNumber__JF5Iy'][text()='" + x + "']"
print(date)
b = driver.find_element(By.XPATH,date)
b.click()
sleep(5)

------------------------------------------------------------------------
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

desired_caps = {
    "appium:options" :
        {
            "appium:appPackage": "ir.flytoday",
            "appium:appActivity": "ir.flytoday.MainActivity",
            "appium:automationName": "UiAutomator2"
        } ,
    "platformName": "Android"
}

appium_server = "http://127.0.0.1:4723"
appium_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.XPATH,value='//*[@text="Allow"]').click()
driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text="هتل"]').click()
sleep(5)
driver.find_elements(by=AppiumBy.CLASS_NAME,value="android.widget.Button")[0].click()
sleep(1)
el1 = driver.find_elements(by=AppiumBy.CLASS_NAME,value="android.widget.EditText")[0]
el1.send_keys('تهران')
sleep(5)
driver.tap([(906,449)])
sleep(10)
driver.find_element(by=AppiumBy.XPATH,value='//*[@text="جستجو"]').click()
sleep(20)
driver.quit()
