from utils.utils import generate_string()
from utils.utils import generate_mail()
Feature: register on reserved website

  Scenario: test register successfully
    Given open the register page
    When the user type email "email"
    And the user type firstname "firstname"
    And the user type lastname "lastname"
    And the user type password "password"
    And the user click Create Account button
    Then the user is redirected to checkout
    And the user is logged in with "firstname"

