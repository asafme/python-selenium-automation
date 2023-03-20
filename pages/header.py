from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_pages import Page


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDER_ICON = (By.CSS_SELECTOR, "a[href*=nav_orders_first")
    CART_ICON = (By.CSS_SELECTOR, "span.nav-cart-icon")
    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href*='/New-Arrivals/']")
    DEALS = (By.CSS_SELECTOR, "div.mega-menu")
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_on_order(self):
        self.click(*self.ORDER_ICON)

    def click_on_cart(self):
        self.click(*self.CART_ICON)

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_deals_shown(self):
        self.wait_for_element_appear(*self.DEALS)

    def select_department(self):
        department_dd = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_dd)
        select.select_by_value('search-alias=amazonfresh')