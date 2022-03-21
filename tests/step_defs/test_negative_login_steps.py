from pytest_bdd import scenarios, when, then, given, parsers
from pages.register_page import RegisterPage

# Scenarios
scenarios('../features/test_negative_login.feature')


# steps
@given('open the register page')
def open_page(browser):
    register_page = RegisterPage(browser)
    register_page.load_page()

@when(parsers.cfparse('the following credentials "{email}","{firstname}","{lastname}","{password}" are used'))
def login(browser, email, firstname, lastname, password):
    register_page = RegisterPage(browser)
    register_page.login(email, firstname, lastname, password)

@then(parsers.cfparse('a "{warning}" should be displayed'))
def is_warning_displayed(browser, warning):
    register_page = RegisterPage(browser)
    register_page.is_warning_displayed(warning)