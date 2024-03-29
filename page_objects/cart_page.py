from seleniumbase import BaseCase

class CartPage(BaseCase):
    converse_add_to_cart_btn ="a[aria-label='Add “Converse” to your cart']"
    cart_count_text = "ul[class='header-action-list'] span[class='count']"
    subtotal_text ="td[class='product-subtotal']"
    product_quantity_input = "input[@id^='quantity']"
    update_cart_btn = "button[value='Update cart']"
    loading_overlay = ".woocommerce-cart-form div[class*='blockOverlay']"

    def open_page(self):
        self.open("https://practice.automationbro.com/cart/")