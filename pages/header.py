from selenium.webdriver.common.by import By
from pages.base_pages import Page


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDER_ICON = (By.CSS_SELECTOR, "a[href*=nav_orders_first")
    CART_ICON = (By.CSS_SELECTOR, "span.nav-cart-icon")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_on_order(self):
        self.click(*self.ORDER_ICON)

    def click_on_cart(self):
        self.click(*self.CART_ICON)
