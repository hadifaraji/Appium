import random


class City:

    def __init__(self, driver):
        self.driver = driver

    def click_on_city(self,AppiumBy, sleep):
        click_on_city = self.driver.find_element(by=AppiumBy.CSS_SELECTOR, value=".android.widget.Button:nth-child(0)")
        click_on_city.click()
        sleep(6)
        get_listof_city = self.driver.find_elements(by=AppiumBy.XPATH, value='//*[@class = "android.view.View"]')
        choice_by_random = random.choice(get_listof_city)
        choice_by_random.click()
        sleep(2)
