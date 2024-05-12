from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
from datetime import datetime
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

appium_server = "http://127.0.0.1:4723"
appium_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(10)
Accept_Alert = driver.find_element(by=AppiumBy.XPATH,value='//*[@text="Allow"]')
Accept_Alert.click()
click_on_Hotel = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=', هتل')
click_on_Hotel.click()
sleep(5)
# new code
date_of_login = driver.tap([(995,608)])
sleep(10)
date_list_of_day = driver.find_elements(by=AppiumBy.CLASS_NAME, value="android.view.View")
sleep(1)
enable_day = []
for day in date_list_of_day:
    get_value = day.get_attribute('text')
    if get_value == 'null':
        continue
    enable_day.append(datetime.strptime(get_value, "%d %B %Y"))
x = random.choice(enable_day)
print(x)

driver.quit()
