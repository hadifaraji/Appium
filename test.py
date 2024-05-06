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

