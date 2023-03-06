from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import when, given, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")

@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

@then('Verify user can click through colors')
def verify_user_can_view_colors(context):
    context.driver.find_element(*COLOR_OPTIONS)

    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors:', all_color_options)

    for color in all_color_options:
        color.click()
