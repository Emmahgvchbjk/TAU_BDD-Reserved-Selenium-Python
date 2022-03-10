from selenium.webdriver.common.by import By


class CheckoutCartPage:
    #URL
    URL = 'https://www.reserved.com/ro/ro/checkout/cart/'

    #locators
    ACCOUNT_INFO_NAME = (By.CSS_SELECTOR, 'div[data-testid="account-info-logged-true"]')


    def __init__(self, browser):
        self.browser = browser

    def check_current_url(self):
        assert self.browser.current_url == self.URL, "Url after create account is not ok"

    def check_firstname(self, firstname):
        assert self.browser.find_element(*self.ACCOUNT_INFO_NAME).text == firstname, "Firstname is not ok"