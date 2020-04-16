from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", \
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", \
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", \
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", \
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", \
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", \
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", \
pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail), \
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", \
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
	#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
	link = f"{link}"
	page = ProductPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()                           # открываем страницу
	page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
	page.add_product_to_basket()          # жмем кнопку добавить в корзину
	page.solve_quiz_and_get_code()
	page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом
	page.should_be_price_in_basket_equal_price_of_product()      # проверяем что цена в корзине такая же что и у продукта

@pytest.mark.skip(reason="module 4.3 step 6 -- expected fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
	page = ProductPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()                           # открываем страницу
	page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
	page.add_product_to_basket()          # жмем кнопку добавить в корзину
	page.should_not_be_success_message()
def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
	page = ProductPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()                           # открываем страницу
	page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
	page.should_not_be_success_message()
@pytest.mark.skip(reason="module 4.3 step 6 -- expected fail")
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
	page = ProductPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()                           # открываем страницу
	page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
	page.add_product_to_basket()          # жмем кнопку добавить в корзину
	page.should_success_message_disappear()


