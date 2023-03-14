# Created by jessicamenashe at 2/18/23
Feature: Amazon Search Tests
  # Enter feature description here

  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Input text coffee
    When Click on search button
#    Then Verify that text "coffee" is shown