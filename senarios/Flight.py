from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
import random

desired_caps = {
    "appium:options" :
        {
            "appium:appPackage": "ir.flytoday",
            "appium:appActivity": "ir.flytoday.MainActivity",
            "appium:automationName": "UiAutomator2"
        } ,
    "platformName": "Android"
}

appium_server = 'http://127.0.0.1:4723'
appium_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(15)
driver.find_element(by=AppiumBy.XPATH,value='//*[@text="Allow"]').click()
sleep(5)
driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.view.ViewGroup')[5].click()
sleep(5)
driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.Button')[2].click()
sleep(5)
el1 = driver.find_elements(by=AppiumBy.XPATH,value="//*[@class = 'android.view.View']")
el2 = random.choice(el1)
el2.click()
sleep(5)
