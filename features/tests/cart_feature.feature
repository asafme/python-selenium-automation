# Created by jessicamenashe at 2/20/23
Feature: Amazon cart verification

  Scenario: User can add a product to cart
    # Enter steps here

  Given Open Amazon's page
  When Input text Roblox Gift Card
  When Click on the search button
  And Click on the first product
  And Click on add to cart button
  And Open cart page
  Then Verify cart has 1 product
