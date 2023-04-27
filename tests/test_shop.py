from selenium.common import NoSuchElementException

from page_objects.shop_page import ShopPage

class ShopTest(ShopPage):
    def test_search_products(self):

        self.open_page()

        # search product
        self.send_keys(self.search_input, "Beer")
        self.click(self.search_btn)

        #assert product image
        try:
            self.assert_element(self.product_img)
        except NoSuchElementException:
            self.assert_text("No products were found matching your selection.", self.no_product_text)

