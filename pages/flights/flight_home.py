import time
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class FlightHomePage(BasePage):
    def select_from_city(self, city_query: str, city_full_name: str):
        self.click_element(By.CSS_SELECTOR, "label[for='fromCity']")
        from_input: WebElement = self.find_element(By.XPATH, "//input[@placeholder= 'From']")
        from_input.clear()
        from_input.send_keys(city_query)

        suggestions: list[WebElement] = self.find_elements(By.CSS_SELECTOR, "li.react-autosuggest__suggestion")
        time.sleep(5)
        for item in suggestions:
            if city_full_name in item.text:
                self.driver.execute_script("arguments[0].click();", item)
                break

    def select_to_city(self, city_query: str, city_full_name: str):
        self.click_element(By.CSS_SELECTOR, "label[for='toCity']")
        to_input: WebElement = self.find_element(By.XPATH, "//input[@placeholder='To']")
        to_input.clear()
        to_input.send_keys(city_query)

        suggestions: list[WebElement] = self.find_elements(By.CSS_SELECTOR, "li.react-autosuggest__suggestion")

        for item in suggestions:
            if city_full_name in item.text:
                self.driver.execute_script("arguments[0].click();", item)
                break

    def select_date(self, departure_date: str, return_date: str):

        self._select_single_date(departure_date)
        self.click_element(By.XPATH,"//div[contains(@class,'reDates')]")

    def _select_single_date(self, date_value: str):
        date_xpath: str = f"//div[@aria-label='{date_value}']"


        date_element: WebElement = self.find_element(By.XPATH, date_xpath)
        self.driver.execute_script("arguments[0].click();", date_element)
        print(f"Date selected: {date_value}")



    def numb_travellers_class(self, adults: int,  numb_kids: int, numb_infants: int, travellers_class: int):
        # ---------clicking on Travellers tab-----------
        self.click_element(By.XPATH, "//label[@for='travellers']")
        print("Travellers tab clicked.")
        # ---------Number of Adults Travellers 12+ age-----------
        self.click_element(By.CSS_SELECTOR, f"li[data-cy='adults-{adults}']")
        if adults == 1:
            print(f"Selected {adults} adult Traveller.")
        elif adults > 1:
            print(f"Selected {adults} adults Travellers.")
        else:
            print(f"No Traveller Selected.")

        #---------Number of kids Travellers (2-12) age-----------
        self.click_element(By.CSS_SELECTOR, f"li[data-cy='children-{numb_kids}']")
        if numb_kids == 1:
            print(f"Selected {numb_kids} kid Traveller.")
        elif numb_kids > 1:
            print(f"Selected {numb_kids} kids Travellers.")
        else:
            print(f"No kids Traveller Selected.")
        #---------Number of Infants Travellers (0-2) age-----------
        self.click_element(By.CSS_SELECTOR, f"li[data-cy='infants-{numb_infants}']")
        if numb_infants == 1:
            print(f"Selected {numb_infants} infant Traveller.")
        elif numb_infants > 1:
            print(f"Selected {numb_infants} infants Travellers.")
        else:
            print(f"No infant Traveller Selected.")
        # ---------Select class-----------
        self.click_element(By.CSS_SELECTOR, f"li[data-cy='travelClass-{travellers_class}']")
        print(f"Selected {travellers_class} class.")

        #----------Apply Button-----------
        self.click_element(By.XPATH, "//button[normalize-space()='APPLY']")
        # self.driver.execute_script("arguments[0].scrollIntoView({block: '700'});", apply_btn)
        # self.driver.execute_script("arguments[0].click();", apply_btn)
        print("apply button clicked")

    def search_button(self):
        self.click_element(By.CSS_SELECTOR, ".primaryBtn.font24.latoBold.widgetSearchBtn")
        print("Navigation confirmed: flight results page.")