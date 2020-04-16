from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color")
	ADDED_PRODUCT_IN_BASKET_MSG = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in strong")
	BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
	ADDED_PRODUCT_SUCCESS_MSG = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in")