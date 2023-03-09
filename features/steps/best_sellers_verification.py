from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import when, given, then
from time import sleep

@given('Open Amazon Best Sellers Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

