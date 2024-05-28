from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
from modules.click_on_city import City
from modules.date_of_login import Date

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
City(driver).click_on_city_in_flight_source(AppiumBy, sleep)
City(driver).click_on_city_in_flight_destination(AppiumBy, sleep)
Date(driver).departure_date_in_flight(AppiumBy, sleep)
click_on_searchBox = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="جستجو"]').click()
sleep(25)

driver.quit()