from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
from modules.click_on_city import City
from modules.date_of_login import Date

desired_caps = {
    "appium:options":
        {
            "appium:appPackage": "ir.flytoday",
            "appium:appActivity": "ir.flytoday.MainActivity",
            "appium:automationName": "UiAutomator2"
        },
    "platformName": "Android"
}

appium_server = "http://127.0.0.1:4723"
appium_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
Accept_Alert = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Allow"]')
Accept_Alert.click()
click_on_Hotel = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=', هتل')
click_on_Hotel.click()
sleep(2)
City(driver).click_on_city(AppiumBy, sleep)
sleep(5)
Date(driver).date_of_login(AppiumBy, sleep)
sleep(5)
click_on_searchBox = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="جستجو"]')
click_on_searchBox.click()
sleep(25)
driver.quit()