from selenium.webdriver.common.by import By
from behave import  given, when, then


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-count-container")


@then('Verify that empty cart {expected_result} is shown' )
def verify_cart_result(context, expected_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-count")
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
