from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import when, given, then
from time import sleep

TOP_LINKS = (By.CSS_SELECTOR, "#zg_header ul li")
HEADER = (By.CSS_SELECTOR, "#zg_banner_text")

@given('Open Amazon Best Sellers')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('User can click through top links and verify correct page opens')
def click_through_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for i in range(len(top_links)):
        link_to_click = context.driver.find_elements(*TOP_LINKS)[i]
        link_text = link_to_click.text
        print(link_text)

        link_to_click.click()

        header_text = context.driver.find_element(*HEADER).text
        print(header_text)
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'
