from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open Amazon Homepage')
def open_amazon_page(context):
    context.app.main_page.open_main()

@when('Click on Orders')
def click_on_orders (context):
    # context.driver.find_element(By.CSS_SELECTOR, "a[href*=nav_orders_first").click()
    context.app.header.click_on_order()

@then('Verify {expected_result} is opened')
def verify_page_opened(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'
