import time
from selenium import webdriver
from pages.auth.login_page import LoginPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.makemytrip.global/?cc=ca")

login_page= LoginPage(driver)
login_page.close_popup()

login_page.login("test@gmail.com", "test@123")

time.sleep(5)
driver.quit()