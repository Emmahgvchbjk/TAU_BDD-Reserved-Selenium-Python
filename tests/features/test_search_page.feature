Feature: search on website

  Scenario Outline: check search functionality
    Given open the search page
    When the user types "<item>" in the search bar
    Then each result contains "<item>" in name

  Examples: Searched item
       | item|
       | pijama |
       | rochie |
       | bluza |