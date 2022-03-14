from selenium.webdriver.common.by import By

class SearchPage:

    URL = "https://www.reserved.com/ro/ro/"
    SEARCH_BAR = (By.CSS_SELECTOR, "div[data-testid='search-input']")
    SEARCH_RESULTS_ITEMS = (By.CLASS_NAME, "hit-item__Title-cz15ax-4 bDBiSH")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-testid='search-button']")
    ACCEPT_COOKIES_BUTTON = (By.ID, "cookiebotDialogOkButton")
    search_results_list = []
    i = 0
    nr = 0

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def search_product(self, searched_item):
        self.browser.find_element(*self.SEARCH_BAR).send_keys(searched_item)

    def get_check_results(self):
        self.search_results_list = self.browser.find_elements(*self.SEARCH_RESULTS_ITEMS)

    def check_results(self):
        substring = 'pijama'
        for self.i in self.search_results_list:
            if substring in self.i:
                self.nr += 1
        if self.nr == len(self.search_results_list):
            print("all results displayed are correct")
        else:
            print("not all the results are not correct")




