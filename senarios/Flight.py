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
accept_Alert = driver.find_element(by=AppiumBy.XPATH,value='//*[@text="Allow"]')
accept_Alert.click()
sleep(5)
click_on_flight = driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.view.ViewGroup')[5]
click_on_flight.click()
sleep(5)
click_on_source = driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.Button')[2]
click_on_source.click()
sleep(5)
get_listof_city = driver.find_elements(by=AppiumBy.XPATH,value="//*[@class = 'android.view.View']")
choice_by_random = random.choice(get_listof_city)
choice_by_random.click()
sleep(2)
click_on_destination = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text(" مقصد")')
click_on_destination.click()
sleep(2)
get_listof_cityy = driver.find_elements(by=AppiumBy.XPATH,value="//*[@class = 'android.view.View']")
choice_by_randomm = random.choice(get_listof_cityy)
choice_by_randomm.click()
sleep(2)