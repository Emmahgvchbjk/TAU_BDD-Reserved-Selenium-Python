from pytest_bdd import scenarios, when, then, given, parsers
from pages.search_page import SearchPage

# Scenarios
scenarios('../features/test_search_page.feature')


# steps
@given('open the search page')
def open_page(browser):
    search_page = SearchPage(browser)
    search_page.load_page()


@when(parsers.cfparse('the user types "pijama" in the search bar'))
def search_product(browser):
    search_page = SearchPage(browser)
    searched_item = "pijama"
    search_page.search_product(searched_item)


@then(parsers.cfparse('the items that have the word "pijama" in title are displayed'))
def check_results(browser):
    search_page = SearchPage(browser)
    search_page.check_results()