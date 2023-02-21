
from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input text coffee')
def input_search_word(context):
    context.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys('coffee')


@when("Click on search button")
def step_impl(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
