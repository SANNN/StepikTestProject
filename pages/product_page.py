from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
	def should_be_add_to_cart_button(self):
		element = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		assert element, f"Button 'Add to cart' is not presented"
	def add_product_to_basket(self):
		add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		add_to_basket.click()
	def should_be_success_message(self):
		time.sleep(4)
		add_to_basket_element = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MSG)
		add_to_basket_msg = add_to_basket_element.text
		product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
		product_name = product_name_element.text
		assert product_name in add_to_basket_msg, \
		f"Message about add product in basket is not correct"
		print(f"Product '{product_name}' in your basket")
	def should_be_price_in_basket_equal_price_of_product(self):
		# Сначала проверяем, что элементы присутствуют на странице
		assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), (
			"Message basket total is not presented")
		assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
			"Product price is not presented")
		product_price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
		product_price = product_price_element.text
		basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
		assert product_price in basket_price, f"Price in basket is NOT equal to price of product"