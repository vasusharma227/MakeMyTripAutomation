from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HotelHomePage(BasePage):
    def search_hotel(self, city_name):
        self.click_element(By.ID, "city")
        input_box = self.click_element(By.XPATH, "//input[@placeholder='Enter city/Hotel/Area']")
        input_box.clear()
        input_box.send_keys(city_name)
        # Add suggestions loop like flight if needed
