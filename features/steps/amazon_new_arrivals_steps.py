from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from behave import given, when, then

@given('Open Amazon Fashion page')
def open_fashion_url(context):
    context.app.main_page.open_fashion_url()


@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.header.hover_new_arrivals()


@then('Verify user sees deals')
def verify_deals_shown(context):
    context.app.header.verify_deals_shown()

