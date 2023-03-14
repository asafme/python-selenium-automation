from selenium.webdriver.common.by import By
from pages.base_pages import Page


class SearchResult(Page):
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    ADD_TO_CART = (By.ID, 'add-to-cart-button')
    CLICK_CART = (By.CSS_SELECTOR, "a[href='/gp/cart/view.html?ref_=sw_gtc']")
    VERIFY_SUBTOTAL = (By.CSS_SELECTOR, "#sc-subtotal-label-buybox")

    # def verify_search_results(self, expected_text):

    def click_first_product(self):
        self.click(*self.PRODUCT_PRICE)

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def click_on_cart(self):
        self.click(*self.CLICK_CART)

    def verify_subtotal(self, expected_amount):
        # self.verify_subtotal(expected_amount, *self.VERIFY_SUBTOTAL)
        actual_text = self.find_element(*self.VERIFY_SUBTOTAL).text
        expected_text = f"Subtotal ({expected_amount} item):"
        assert expected_text in actual_text, f"Expected Text not found"
