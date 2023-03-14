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
    context.app.main_page.open_main_url()


@when('Input text {text}')
def input_search_word(context, text):
    context.app.header.input_search_text(text)


@when('Click on the search button')
def click_search_icon(context):
    context.app.header.click_search()


@when("Click on the first product")
def click_first_product(context):
    context.app.search_result.click_first_product()


@when('Click on add to cart button')
def click_add_to_cart(context):
    context.app.search_result.click_add_to_cart()

@when('Click on cart')
def click_on_cart(context):
    context.app.search_result.click_on_cart()


@then('Verify cart has {expected_amount} product')
def verify_cart_count(context, expected_amount):
    context.app.search_result.verify_subtotal(expected_amount)



# @then('Verify cart has {expected_amount} product')
# def verify_cart_count(context, expected_amount):
#     expected_amount = int(expected_amount)
#     context.driver.find_element(*VERIFY_SUBTOTAL)
