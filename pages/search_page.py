from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:

    URL = "https://www.reserved.com/ro/ro/"
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-testid='search-open-button']")
    SEARCH_BAR = (By.CSS_SELECTOR, "input[type='search']")
    SORTING_DROP_DOWN = (By.CSS_SELECTOR, "[data-testid='sorting']")
    SEARCH_RESULTS_ITEMS = (By.CLASS_NAME, "hit-item__Title-cz15ax-4 bDBiSH")
    ACCEPT_COOKIES_BUTTON = (By.ID, "cookiebotDialogOkButton")

    def _init_(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def click_search_button(self):
        self.browser.find_element(*self.SEARCH_BUTTON).click()

    def search_product(self, searched_item):
        self.browser.find_element(*self.SEARCH_BAR).send_keys(searched_item)
        # nu imi mergea fara enter tot timpul
        self.browser.find_element(*self.SEARCH_BAR).send_keys(Keys.ENTER)
        # aici am pus wait sa astepte sa se incarce pagina cu produse, am pus un wait dupa dropdownul ala ce sorteaza
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.SORTING_DROP_DOWN))

    # aici am schimbat sa imi returneze o lista sa o putem folosi mai jos s aluam textul
    def get_results_list(self):
        return self.browser.find_elements(*self.SEARCH_RESULTS_ITEMS)

    def check_results(self, searched_item):
        for i in self.get_results_list():
            assert searched_item.lower() in i.text.lower(), "Result is not ok"