from selenium.webdriver.common.by import By
from behave import given, when, then

AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_TO_CART =  (By.ID, 'add-to-cart-button')
CLICK_CART = (By.CSS_SELECTOR, "a[href='/gp/cart/view.html?ref_=sw_gtc']")
VERIFY_SUBTOTAL = (By.CSS_SELECTOR, "#sc-subtotal-label-buybox")

@given('Open Amazon website')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input text {text}')
def input_search_word(context, text):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(text)


@when('Click on the search button')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_ICON).click()


@when("Click on the first product")
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Click on add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()

@when('Click on cart')
def click_on_cart(context):
    context.driver.find_element(*CLICK_CART).click()


@then('Verify cart has {expected_amount} product')
def verify_cart_count(context, expected_amount):
    expected_amount = int(expected_amount)
    context.driver.find_element(*VERIFY_SUBTOTAL)
