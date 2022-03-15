from pytest_bdd import scenarios, when, then, given, parsers
from pages.search_page import SearchPage

# Scenarios
scenarios('../features/test_search_page.feature')


# steps
@given('open the search page')
def open_page(browser):
    search_page = SearchPage(browser)
    search_page.load_page()


@when(parsers.cfparse('the user types "{searched_item}" in the search bar'))
def search_product(browser, searched_item):
    # dam searched item ca arametru s aputem cauta cu orice valoare vrem noi ca daca nu tot timpul
    # scrie pijama
    search_page = SearchPage(browser)
    search_page.click_search_button()
    search_page.search_product(searched_item)


@then(parsers.cfparse('each result contains "{searched_item}" in name'))
def check_results (browser, searched_item):
    search_page = SearchPage(browser)
    search_page.check_results(searched_item)