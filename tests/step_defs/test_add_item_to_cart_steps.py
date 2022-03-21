from pytest_bdd import scenarios, when, then, given, parsers
from pages.search_page import SearchPage

# Scenarios
scenarios('../features/test_add_item_to_cart.feature')

# steps
@given('open the search page')
def open_page(browser):
    search_page = SearchPage(browser)
    search_page.load_page()

@when(parsers.cfparse('the user types "{searched_item}" in the search bar'))
def search_product(browser, searched_item):
    search_page = SearchPage(browser)
    search_page.click_search_button()
    search_page.search_product(searched_item)

@when (parsers.cfparse('the user clicks on a random search result'))
def select_item(browser):
    search_page = SearchPage(browser)
    search_page.select_item()

@when(parsers.cfparse('the item picked contains "{searched_item}" in name'))
def check_results(browser, searched_item):
    search_page = SearchPage(browser)
    search_page.check_results(searched_item)

@when(parsers.cfparse('the user picks a size'))
def select_size(browser):
    search_page = SearchPage(browser)
    search_page.select_size()

@when(parsers.cfparse('the user clicks on "ad item to cart" and on "finalizeaza comanda"'))
def finalizeaza_comanda(browser):
    search_page = SearchPage(browser)
    search_page.finalizeaza_comanda()

@then(parsers.cfparse('the sections "esti membru nou" and "este prima ta vizita" appear'))
def check_page(browser):
    search_page = SearchPage(browser)
    search_page.check_page()