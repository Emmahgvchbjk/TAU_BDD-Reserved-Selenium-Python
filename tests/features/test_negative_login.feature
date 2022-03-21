Feature: register on reserved website

  Scenario Outline: register with wrong credentials on reserved website
    Given open the register page
    When the following credentials "<email>","<firstname>","<lastname>","<password>" are used
    Then a "<warning>" should be displayed
    Examples:
      | email            | firstname | lastname | password | warning                                        |
      | fvg              | ccgf      | ggdgt    | fdgththt | Vă rugăm să introduceți numai caractere valide |
      | fdvdvfd@gmai.com | 32        | bgfbfvf  | vfdvdd   | Vă rugăm să introduceți numai caractere valide |
      | vdvfd@gmai.com   | hgfbf     | 3        | vdfvdfd  | Vă rugăm să introduceți numai caractere valide |