# Created by jessicamenashe at 3/20/23
Feature: Amazon Departments Verification


 Scenario: User can select and search from a department
    Given Open Amazon
    When Select department Amazon Fresh
    And Input text Grapes
    And Click on the search button
    Then Verify Amazon Fresh department is selected