from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

service = Service('/Users/jessicamenashe/Desktop/automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

#Amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

#Your name field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#Mobile or email field
driver.find_element(By.CSS_SELECTOR, '#ap_email')

#password
driver.find_element(By.CSS_SELECTOR, '#ap_password')

#reenter password
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#continue
driver.find_element(By.CSS_SELECTOR, '#continue')

#privacy notice
driver.find_element(By.CSS_SELECTOR, '#a[href*="ap register_notification_privacy_notice"]')

#conditions of use
driver.find_element(By.CSS_SELECTOR, '#a[href*="ap_register_notification_privacy_notice"]' )

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when ('Click on Orders')
def click_on_orders (context):
    context.driver.find_element(By.XPATH, "//h2[text()='& Orders']").click()


@then ('Verify {expected_result} is opened')
def verify_page_opened(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'


#Verify that cart is empty
@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-count-container")


@then('Verify that empty cart {expected_result} is shown')
def verify_cart_result(context, expected_result):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-count")
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
