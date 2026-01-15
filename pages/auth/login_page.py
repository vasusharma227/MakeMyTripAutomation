import time
from typing import Tuple
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, "p[data-cy='LoginHeaderText']")
    EMAIL_ID_INPUT: Tuple[str, str] = (By.CSS_SELECTOR , "input[placeholder='Enter email or mobile number']")
    CHECKBOX: Tuple[str, str]= (By.CSS_SELECTOR, "#global-consent-box")
    CONTINUE_BTN: Tuple[str, str] = (By.CSS_SELECTOR, "button[type='button']")
    PASSWORD_INPUT: Tuple[str, str] = (By.CSS_SELECTOR, "#password")
    SUBMIT_BTN: Tuple[str, str] = (By.CSS_SELECTOR, "button[type = 'submit']")
    def login(self, email: str, password: str):
        self.click(self.LOGIN_BUTTON)
        self.type(self.EMAIL_ID_INPUT, email)

        self.click(self.CHECKBOX)
        time.sleep(2)
        self.click(self.CHECKBOX)
        self.click(self.CONTINUE_BTN)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BTN)

    #---------Password-----------
    # def click_login_button(self):
    #     self.click(self.LOGIN_BUTTON)
    #
    # # ---------email-----------
    # def enter_email(self, email):
    #     self.type(self.EMAIL_ID_INPUT, email)
    #
    # #---------term and condition checkbox-----------
    # def accept_terms_checkbox(self):
    #     self.click(self.CHECKBOX)
    #     #self.find_element(By.CSS_SELECTOR, "#user-consent-checkbox").clear()
    #
    # # ---------continue button-----------
    # def click_continue_button(self):
    #     self.click(self.CONTINUE_BTN)
    #
    # # ---------Password-----------
    # def enter_password(self, password):
    #     self.type(self.PASSWORD_INPUT, password)
    #
    # def submit_btn(self):
    #     # ---------Submit button-----------
    #     self.click(self.SUBMIT_BTN)
