# Created by jessicamenashe at 2/20/23
Feature: Amazon cart verification

  Scenario: User can add a product to cart
    # Enter steps here

  Given Open Amazon website
  When Input text Roblox Gift Card
  When Click on the search button
  When Click on the first product
  When Click on add to cart button
  When Click on cart
  Then Verify cart has 1 product
