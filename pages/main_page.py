from pages.base_pages import Page


class MainPage(Page):

    def open_main_url(self):
        self.open_url('https://www.amazon.com/')


    def open_fashion_url(self):
        self.open_url('https://www.amazon.com/gp/product/B074TBCSC8')