# Created by jessicamenashe at 3/8/23
Feature: Verify that Best Sellers links work


  Scenario: User can access each Best Sellers Link
    Given Open Amazon Best Sellers Page
    Then Verify each link opens correct page
