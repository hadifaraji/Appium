# پنهان کردن صفحه کیبورد
# driver.hide_keyboard()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# ساخت تاریخ رندوم
# from datetime import date
# import random
# start_date = date.today().replace(day=1, month=1).toordinal()
# end_date = date.today().toordinal()
# random_day = date.fromordinal(random.randint(start_date, end_date))
# print(f"Random date: {random_day}")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# تایپ کردن در فیلد بدون send_Keys

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
from datetime import datetime
import random

desired_caps = {
    "platformName": "Android",
    "appium:options": {
        "appPackage": "io.appium.android.apis",
        "appActivity": ".ApiDemos",
        "automationName": "UiAutomator2"
    }
}
appium_server = 'http://127.0.0.1:4723'
appium_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(3)

driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Views').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Date Widgets').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, '1. Dialog').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'change the date').click()

# def get_select_date(driver) :
#     select_date_desc = driver.find_element(by=AppiumBy.CSS_SELECTOR, value='[resource-id="android:id/month_view"] > .android.view.View:checked').get_attribute('content-desc')
#     return datetime.strptime(select_date_desc, '%d %B %Y')

date_objects = []
date_elements = driver.find_element(AppiumBy.ID, 'android:id/month_view').find_elements(AppiumBy.CLASS_NAME, 'android.view.View')
for day in date_elements:
    date_string = day.get_attribute('content-desc')
    if date_string == 'null':
        continue
    date_objects.append(datetime.strptime(date_string, "%d %B %Y"))
x = random.choice(date_objects)
print(x)

-----------------------------------------------
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
#x = random.choice(test)
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


from datetime import date
import random

start_date = date.today().replace(day=1, month=1)#.toordinal()
print(start_date)
end_date = date.today().toordinal()
random_day = date.fromordinal(random.randint(start_date, end_date))

print(f"Random date: {random_day}")


--------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random


# def wait_until_page_successfully_laoded():
#     for i in range(10):
#         try:
#             state = driver.execute_script("return document.readyState")
#             assert state == 'complete'
#             print("page is loaded")
#         except:
#             sleep(0.5)


driver = webdriver.Firefox()
driver.get("https://www.flytoday.ir/")
#wait_until_page_successfully_laoded()
source = (driver.find_element(By.XPATH,"//*[text()='مبدا']/../.."))
source.click()
sleep(3)
city_list = driver.find_elements(By.XPATH,"//*[@class='option_title__BYCIp']")
#print(random.choice(city_list))
selected = (random.choice(city_list))
selected.click()

start_date = driver.find_element(By.XPATH,"//*[text()='تاریخ رفت']")
start_date.click()

days = driver.find_elements(By.XPATH,"(//*[@class='month_month__Z9X2p'])[1]//button[contains(@class, 'day_day__G5CoD')]")
days_count = (len(days))

enable_days = []

for i in range (days_count):

    if days[i].is_enabled():
        enable_days.append(days[i])
        # print(f"enable :+ {days[i].text}")
    else:
        None
        # print(f"disable :+ {days[i].text}")
    # print(days[i].text)
print(enable_days)
selected_date = random.choice(enable_days)
print (selected_date)
selected_date.click()
sleep(5)

# driver = webdriver.Firefox()
# driver.get("https://www.java.com/en/")
# def wait_until_page_successfully_laoded(timeout=10):
#     for i in range(timeout*2):
#         try:
#             state = driver.execute_script("return document.readyState")
#             assert state == 'complete'
#             print("page is loaded")
#             return
#         except:
#             sleep(0.5)
#             print('Loading...')
#
#
# wait_until_page_successfully_laoded()
