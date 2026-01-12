from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 20):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, timeout)

    def click_element(self, by: By, locator: str) -> WebElement:
        element: WebElement = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()
        return element

    def find_element(self, by: By, locator: str) -> WebElement:
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def find_elements(self, by: By, locator: str) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located((by, locator)))

    def close_popup(self):
        try:
            self.click_element(By.XPATH, "//span[contains(@class, 'commonModal__close')]")
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "commonModal__overlay")))
            print("Popup Closed.")
        except:
            print("No popup found or already closed")




