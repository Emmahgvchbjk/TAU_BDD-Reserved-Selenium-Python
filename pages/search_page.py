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
    ADAUGA = (By.CSS_SELECTOR, 'data-selen="add-coupon-code"')

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

    def get_results_list(self):
        return self.browser.find_elements(*self.SEARCH_RESULTS_ITEMS)

    def check_results(self, searched_item):
        for i in self.get_results_list():
            assert searched_item.lower() in i.text.lower(), "Result is not ok"

    def select_item(self):
        list = self.get_results_list()
        el = random.randint(1, len(list))
        element = list[el]
        ActionChains(self.broser).move_to_element(element).click().perform()
        print(element)
        self.browser.find_element(By.XPATH, '//div[text()="%s"]' % element)

    def select_size(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.SIZE_BAR))
        self.browser.find_element(*self.SIZE_BAR).click()
        self.browser.find_element(*self.SIZE_AVAILABLE).click()

    def add_to_cart(self):
        self.browser.find_element(*self.ADD_TO_CART_BUTTON).click()
        self.browser.find_element(*self.FINALIZEAZA_COMANDA_BUTTON).click()

    def adauga(self):
        self.browser.find_element(*self.ADAUGA).click()
