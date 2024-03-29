from page_objects.cart_page import CartPage
from selenium.webdriver.common.keys import Keys

class CartTest(CartPage):
    def setUp(self):
        super().setUp()
        self.open("https://practice.automationbro.com/shop/")


    def test_add_to_cart(self):

        # add item to the cart
        self.click(self.converse_add_to_cart_btn)
        #assert product is added to the cart
        self.assert_text('1', self.cart_count_text)
        #open cart page
        self.open_page()
        # get current subtotal
        text = self.get_text(self.subtotal_text)
        print(text)
        # change cart quantity

        self.set_value(self.product_quantity_input, '2')
        self.send_keys(self.product_quantity_input, Keys.RETURN)
        self.click(self.update_cart_btn)

        # wait for loading to be completed
        # self.wait_for_element_visible(self.loading_overlay)
        # self.wait_for_element_not_visible(self.loading_overlay)


        # assert subtotal to be different than the original subtotal
        self.wait_for_text("$340.00", self.subtotal_text)
        update_text = self.get_text(self.subtotal_text)

        self.assertNotEquals(text, update_text)
        print(update_text)