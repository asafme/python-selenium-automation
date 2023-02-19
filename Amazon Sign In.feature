# Created by jessicamenashe at 2/19/23
Feature: # Homework 3 Search.feature
  # Enter feature description here

  Scenario: # User can access Sign In page
    Given Open Amazon page
    When Click on Orders
    Then Verify sign on page is opened
    Then Verify sign in header is visible
    Then Verify email input field is present.

