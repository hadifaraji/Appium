from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
import random

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


def click_on_city(driver, AppiumBy, sleep):
    click_on_city = driver.find_element(by=AppiumBy.CSS_SELECTOR, value='.android.widget.Button:nth-child(0)')
    click_on_city.click()
    sleep(6)
    get_listof_city = driver.find_elements(by=AppiumBy.XPATH, value='//*[@class = "android.view.View"]')
    choice_by_random = random.choice(get_listof_city)
    choice_by_random.click()
    sleep(2)

