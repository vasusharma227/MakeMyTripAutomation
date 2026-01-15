from typing import Tuple, List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 20):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, timeout)

    def click(self, locator: Tuple[str, str]) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()


    def type(self, locator: Tuple[str, str], text: str)-> None:
        element: WebElement = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple[str, str])-> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def close_popup(self) -> None: # Added -> None
        try:
            self.click((By.XPATH, "//span[contains(@class, 'commonModal__close')]"))
            self.wait.until(
                EC.invisibility_of_element_located(
                    (By.CLASS_NAME, "commonModal__overlay")
                )
            )
            print("Popup Closed.")
        except Exception:
            print("No popup found or already closed")