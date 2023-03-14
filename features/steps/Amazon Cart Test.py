from selenium.webdriver.common.by import By
from behave import given, when, then

CART_ICON = (By.CSS_SELECTOR, "span.nav-cart-icon")


@given('Open Amazon main page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Click on cart icon')
def click_cart(context):
    # context.driver.find_element(*CART_ICON).click()
    context.app.header.click_on_cart()

@then('Verify {expected_result} present')
def verify_text(context, expected_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.sc-your-amazon-cart-is-empty").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
