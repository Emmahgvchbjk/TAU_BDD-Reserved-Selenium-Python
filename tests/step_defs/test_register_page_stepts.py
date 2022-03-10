from pytest_bdd import scenarios, when, then, given, parsers
from pages.register_page import RegisterPage
from pages.checkout_cart_page import CheckoutCartPage
from utils.utils import CreateStrings

# Scenarios
scenarios('../features/test_register_page.feature')


# steps
@given('open the register page')
def open_page(browser):
    register_page = RegisterPage(browser)
    register_page.load_page()


@when(parsers.cfparse('the user type email {email}'))
def type_email(browser, email):
    register_page = RegisterPage(browser)
    email = CreateStrings.generate_mail(5)
    register_page.type_email(email)


@when(parsers.cfparse('the user type firstname {firstname}'))
def type_firstname(browser, firstname):
    register_page = RegisterPage(browser)
    firstname = CreateStrings.generate_string(7)
    register_page.type_firstname(firstname)


@when(parsers.cfparse('the user type lastname {lastname}'))
def type_lastname(browser, lastname):
    register_page = RegisterPage(browser)
    lastname = CreateStrings.generate_string(7)
    register_page.type_lastname(lastname)


@when(parsers.cfparse('the user type password {password}'))
def type_password(browser, password):
    register_page = RegisterPage(browser)
    password = CreateStrings.generate_string(7)
    register_page.type_password(password)


@when('the user click Create Account button')
def click_create_account_button(browser):
    register_page = RegisterPage(browser)
    register_page.click_create_account_button()


@then('the user is redirected to checkout')
def check_user_is_redirected_to_checkout(browser):
    checkout_cart_page = CheckoutCartPage(browser)
    checkout_cart_page.check_current_url()


@then(parsers.cfparse('the user is logged in with {firstname}'))
def check_user_is_logged_in(browser, firstname):
    checkout_cart_page = CheckoutCartPage(browser)
    checkout_cart_page.check_firstname(firstname)