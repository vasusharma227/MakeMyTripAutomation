import time
from selenium import webdriver
from pages.flights.flight_home import FlightHomePage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.makemytrip.global/?cc=ca")

flight_page = FlightHomePage(driver)
flight_page.close_popup()
time.sleep(1)
driver.execute_script("window.scrollBy(0,120)")


flight_page.select_from_city("tor", "Toronto")
flight_page.select_to_city("del", "New Delhi")
flight_page.select_date("Wed Jan 28 2026","Sat Feb 28 2026")
flight_page.numb_travellers_class(2, 2, 1, 1)
flight_page.search_button()
time.sleep(5)
driver.quit()
