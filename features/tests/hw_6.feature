# Created by jessicamenashe at 3/8/23
Feature: Verify Amazon Privacy Link


  Scenario: User can open and close Amazon Privacy Notice
     Given Open Amazon T&C page
    When  Store Original Windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is visible
    And User can close new window
    And Switch back to original window