from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
from datetime import datetime
import random

desired_caps = {
  "appium:appPackage": "ir.flytoday",
  "appium:appActivity": "ir.flytoday.MainActivity",
  "platformName": "Android",
  "appium:automationName": "UiAutomator2"
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
date_of_login = driver.tap([(962,599)])
sleep(10)
date_list_of_day = driver.find_elements(by=AppiumBy.CSS_SELECTOR, value='.android.widget.Button')
count_of_day = len(date_list_of_day)
enable_days = []
for i in range (count_of_day):
    if date_list_of_day[i].is_enabled():
        enable_days.append(date_list_of_day[i])
    else:
        None
num_selections = 2
selected_date = random.choice(enable_days,num_selections)
selected_date.click()
sleep(2)
click_on_approve = driver.tap([(546,2035)])
sleep(5)

driver.quit()
