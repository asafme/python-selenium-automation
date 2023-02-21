from selenium.webdriver.common.by import By
from behave import  given, when, then




@when ('Click on Orders')
def click_on_orders (context):
    context.driver.find_element(By.XPATH, "//h2[text()='& Orders']").click()


@then ('Verify {expected_result} is opened')
def verify_page_opened(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'
