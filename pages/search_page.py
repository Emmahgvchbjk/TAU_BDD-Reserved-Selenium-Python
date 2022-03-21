import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SearchPage:

    URL = "https://www.reserved.com/ro/ro/"
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-testid='search-open-button']")
    SEARCH_BAR = (By.CSS_SELECTOR, "input[type='search']")
    SORTING_DROP_DOWN = (By.CSS_SELECTOR, "[data-testid='sorting']")
    SEARCH_RESULTS_ITEMS = (By.CLASS_NAME, "hit-item__Title-cz15ax-4 bDBiSH")
    ACCEPT_COOKIES_BUTTON = (By.ID, "cookiebotDialogOkButton")
    SIZE_BAR = (By.CSS_SELECTOR, "div.size-selected")
    SIZE_AVAILABLE = (By.CSS_SELECTOR, "li[data-selen='size']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[data-selen="add-to-cart-button"]')
    FINALIZEAZA_COMANDA_BUTTON = (By.CSS_SELECTOR, 'a[data-selen="cart-confirmation-go-to-checkout"]')
    FINALIZEAZA_COMANDA_BUTTON2 = (By.CSS_SELECTOR, 'button[data-selen="order-link"]')
    SECOND_RESULT =(By.CSS_SELECTOR, 'div[data-testid="products-results"] >  ul > li:nth-of-type(2)')
    SECTION1 = (By.XPATH, "//*[contains(text(), 'membru nou')]")
    SECTION2 = (By.XPATH, "//*[contains(text(), 'prima ta')]")

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def click_search_button(self):
        self.browser.find_element(*self.SEARCH_BUTTON).click()

    def search_product(self, searched_item):
        self.browser.find_element(*self.SEARCH_BAR).send_keys(searched_item)
        self.browser.find_element(*self.SEARCH_BAR).send_keys(Keys.ENTER)
        # aici am pus wait sa astepte sa se incarce pagina cu produse, am pus un wait dupa dropdownul ala ce sorteaza
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.SORTING_DROP_DOWN))
        self.browser.maximize_window()

    def get_results_list(self):
        return self.browser.find_elements(*self.SEARCH_RESULTS_ITEMS)


    def check_results(self, searched_item):
        for i in self.get_results_list():
            assert searched_item.lower() in i.text.lower(), "Result is not ok"

    def select_item(self):
        self.browser.find_element(*self.SECOND_RESULT).click()

    def select_size(self):
        self.browser.find_element(*self.ADD_TO_CART_BUTTON).click()
        self.browser.find_element(*self.SIZE_AVAILABLE).click()

    def finalizeaza_comanda(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.FINALIZEAZA_COMANDA_BUTTON))
        self.browser.find_element(*self.FINALIZEAZA_COMANDA_BUTTON).click()
        self.browser.find_element(*self.FINALIZEAZA_COMANDA_BUTTON2).click()

    def check_page(self):
        self.browser.find_element(*self.SECTION1).is_displayed()
        self.browser.find_element(*self.SECTION2).is_displayed()