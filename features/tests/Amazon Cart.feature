# Created by jessicamenashe at 2/19/23
Feature:  Amazon Cart Test


  Scenario: User can check that cart is empty
    Given Open Amazon main page
    When Click on cart icon
    Then Verify Your Amazon Cart is empty present
