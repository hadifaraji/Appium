import random


class City:

    def __init__(self, driver):
        self.driver = driver

    def click_on_city_in_hotel(self, AppiumBy, sleep):
        click_on_city = self.driver.find_element(by=AppiumBy.CSS_SELECTOR, value='.android.widget.Button:nth-child(0)').click()
        sleep(6)
        get_listof_city = self.driver.find_elements(by=AppiumBy.XPATH, value='//*[@class = "android.view.View"]')
        choice_by_random = random.choice(get_listof_city)
        choice_by_random.click()
        sleep(2)

    def click_on_city_in_flight_source(self, AppiumBy, sleep):
        click_on_source = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.Button')[2].click()
        sleep(5)
        get_listof_city = self.driver.find_elements(by=AppiumBy.XPATH, value="//*[@class = 'android.view.View']")
        choice_by_random = random.choice(get_listof_city)
        choice_by_random.click()
        sleep(2)

    def click_on_city_in_flight_destination(self, AppiumBy, sleep):
        click_on_destination = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text(" مقصد")').click()
        sleep(2)
        get_listof_city = self.driver.find_elements(by=AppiumBy.XPATH, value="//*[@class = 'android.view.View']")
        choice_by_random = random.choice(get_listof_city)
        choice_by_random.click()
        sleep(3)