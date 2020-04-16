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
		added_to_basket_element = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_IN_BASKET_MSG)
		added_to_basket_product = added_to_basket_element.text
		product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
		product_name = product_name_element.text
		assert product_name == added_to_basket_product, \
		f"Added product '{added_to_basket_product}' in basket is not correct '{product_name}'"
		print(f"Product name '{added_to_basket_product}' in basket and product name '{product_name}'")
	def should_be_price_in_basket_equal_price_of_product(self):
		# Сначала проверяем, что элементы присутствуют на странице
		assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), (
			"Message basket total is not presented")
		assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
			"Product price is not presented")
		product_price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
		product_price = product_price_element.text
		basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
		assert product_price == basket_price, f"Price in basket '{basket_price}' is NOT equal to price of product '{product_price}'"
	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_SUCCESS_MSG),\
		"Success message is presented"
	def should_success_message_disappear(self):
		assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_SUCCESS_MSG),\
		"Success message is not disappeared"