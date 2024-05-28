from datetime import datetime
import random


class Date:

    def __init__(self,driver):
        self.driver = driver

    def date_of_login_in_hotel(self, AppiumBy, sleep):
        date_of_login = self.driver.find_element(by=AppiumBy.CSS_SELECTOR, value='.android.widget.Button:nth-child(1)').click()
        sleep(2)
        date_list_of_day = self.driver.find_elements(by=AppiumBy.CSS_SELECTOR, value='.android.widget.Button')
        count_of_day = len(date_list_of_day)
        enable_days = []
        for i in range(count_of_day):
            if date_list_of_day[i].is_enabled():
                enable_days.append(date_list_of_day[i])
            else:
                None
        selected_date = random.choice(enable_days)
        selected_date.click()
        sleep(5)
        click_on_approve = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("تائید")').click()
        sleep(1)

    def departure_date_in_flight(self, AppiumBy, sleep):
        departure_date = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text(" تاریخ رفت 9 خرداد")').click()
        sleep(2)
        date_list_of_day = self.driver.find_elements(by=AppiumBy.CSS_SELECTOR, value='.android.widget.Button')
        count_of_day = len(date_list_of_day)
        enable_days = []
        for i in range(count_of_day):
            if date_list_of_day[i].is_enabled():
                enable_days.append(date_list_of_day[i])
            else:
                None
        selected_date = random.choice(enable_days)
        selected_date.click()
        sleep(5)
        click_on_approve = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("تائید")').click()
        sleep(1)