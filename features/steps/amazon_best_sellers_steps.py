from selenium.webdriver.common.by import By
from behave import given, when, then

HEADER_LINKS = (By.CSS_SELECTOR, "#zg_header ul li")
@given('Open Amazon Best Sellers Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify that headers has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    print('Original Type: ', type(expected_amount))
    expected_amount = int(expected_amount)
    print('Type after converting: ', type(expected_amount))

    header_links = context.driver.find_elements(*HEADER_LINKS)
    print(header_links)
    print('n/Link count: ', len(header_links))
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links, but got {len(header_links)}'


