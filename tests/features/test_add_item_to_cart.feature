Feature: add to cart

  Scenario Outline: check add item to cart
    Given open the search page
    When the user types "<searched_item>" in the search bar
    And the user clicks on a random search result
    And the item picked contains "<searched_item>" in name
    And the user picks a size
    And the user clicks on "ad item to cart" and on "finalizeaza comanda"
    Then the sections "esti membru nou" and "este prima ta vizita" appear

  Examples: Searched item
    | searched_item |
    | tricou        |
    | blugi         |