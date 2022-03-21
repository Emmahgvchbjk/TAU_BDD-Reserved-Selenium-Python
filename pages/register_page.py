import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:

    #URL
    URL = "https://www.reserved.com/ro/ro/customer/account/login/#register"

    #locators
    EMAIL_FIELD = (By.ID, "email_id")
    FIRSTNAME_FIELD = (By.ID, "firstname_id")
    LASTNAME_FIELD = (By.ID, "lastname_id")
    PASSWORD_FIELD = (By.ID, "password_id")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-selen='create-account-submit']")
    ACCEPT_COOKIES_BUTTON = (By.ID, 'cookiebotDialogOkButton')
    WARNING_TEXT = (By.CSS_SELECTOR, 'div.invalid>div')
    WARNING = "Vă rugăm să introduceți numai caractere valide"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def type_email(self, email):
        self.browser.find_element(*self.EMAIL_FIELD).send_keys(email)

    def type_firstname(self, firstname):
        self.browser.find_element(*self.FIRSTNAME_FIELD).send_keys(firstname)

    def type_lastname(self, lastname):
        self.browser.find_element(*self.LASTNAME_FIELD).send_keys(lastname)

    def type_password(self, password):
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_create_account_button(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.CREATE_ACCOUNT_BUTTON)).click()

    def is_warning_displayed(self, warning):
        assert warning in self.browser.find_element(*self.WARNING_TEXT).text

    def login(self, email, firstname, lastname, password):
        self.type_email(email)
        self.type_firstname(firstname)
        self.type_lastname(lastname)
        self.type_password(password)
        self.click_create_account_button()
