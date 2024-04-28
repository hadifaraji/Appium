from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

desired_caps = {
"appium:appPackage": "ir.flytoday",
"appium:appActivity": "ir.flytoday.MainActivity",
"platformName": "Android",
"appium:automationName": "UiAutomator2"
}
appium_server = "http://127.0.0.1:4723"
appium_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.find_element(by=AppiumBy.XPATH,value='//*[@text="Allow"]').click()
driver.find_element(by=AppiumBy.XPATH,value='//*[@text="هتل"]').click()
sleep(5)

driver.quit()