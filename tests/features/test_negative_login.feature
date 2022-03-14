#Feature: register on reserved website
#
#  Scenario Outline: register with wrong credentials on reserved website
#    Given open the register page
#    When the following credentials "<email>","<firstname>" "<lastname>" "<password>" are used:
#
#    Then a "<message>" should be displayed
#    Examples:
#      | email            | firstname | lastname | password | message                     |
#      |                  | ccgf      | ggdgt    | fdgththt | Acest câmp este obligatoriu |
#      | fdvdvfd@gmai.com |           | bgfbfvf  | vfdvdd   | Acest câmp este obligatoriu |
#      | vdvfd@gmai.com   | hgfbf     |          | vdfvdfd  | Acest câmp este obligatoriu |