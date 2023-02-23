# Created by jessicamenashe at 2/21/23
Feature: Amazon Best Sellers Verification
  Scenario: There are 5 Best Sellers links

Given Open Amazon Best Sellers Page
Then Verify that headers has 5 links
