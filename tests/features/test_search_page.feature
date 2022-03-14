Feature: search on website

  Scenario: search for "pijama" items
    Given open the search page
    When the user types "pijama" in the search bar
    Then the items that have the word "pijama" in title are displayed


