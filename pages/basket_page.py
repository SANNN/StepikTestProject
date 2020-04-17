from .base_page import BasePage
from .locators import BasketLocators
import time


class BasketPage(BasePage):
	def go_to_basket_now(self):
		self.openBasket(*BasketLocators.MAIN_BASKET_BUTTON)
	def should_be_no_products_in_basket(self):
		assert self.is_not_element_present(*BasketLocators.ITEMS_TO_BUY), (
			"Product is presented in basket")
	def should_be_empty_basket_message(self):
		basket_msg = self.browser.find_element(*BasketLocators.EMPTY_BASKET_MSG).text
		assert self.is_element_present(*BasketLocators.EMPTY_BASKET_MSG), (
			f"Message about empty basket is missing but found '{basket_msg}'")