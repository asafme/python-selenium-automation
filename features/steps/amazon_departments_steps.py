from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from behave import given, when, then


@given('Open Amazon')
def open_amazon(context):
    context.app.main_page.open_main_url()


@when('Select department Amazon Fresh')
def select_department(context):
    context.app.header.select_department()


@then('Verify Amazon Fresh department is selected')
def verify_selected_dept(context):
    context.app.search_result.verify_selected_dept()