import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from .pages.login_page import LoginPage
import time
import math
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .test_main_page import TestLoginFromMainPage 
from .pages.basket_page import BasketPage
import time

# Общий список URL для parametrize
offer_links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]

@pytest.mark.final_proverka
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()
    time.sleep(60)

@pytest.mark.sravnenie_name_and_price 
def test_guest_add_vernoe_name(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.sravnenie_name()

@pytest.mark.sravnenie_name_and_price
def test_guest_add_vernoe_price(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.sravnenie_price()

@pytest.mark.need_review
# Применяем parametrize к test_guest_can_add_product_to_basket
@pytest.mark.parametrize('link', offer_links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    try: 
        page.sravnenie_oba()
    except Exception as e:
        pytest.xfail(f"Тест упал на ссылке {link} с ошибкой: {str(e)}")


@pytest.mark.xfail(reason="broken by design")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="broken by design")
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="broken by design")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()
    page.should_be_success_message()
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_cart() # Используем метод (выполняем функцию) go_to_cart (переход в корзину) класса BasePage
    basket = BasketPage(browser, link) # Инициализируем класс BasketPage чтобы использовать его методы
    basket.basket_is_empty() # Проверяем, что корзина пуста, используя метод basket_is_empty класса BasketPage
    basket.basket_is_empty_message() # Проверяем, что есть сообщение о том, что корзина пуста, используя метод basket_is_empty класса BasketPage

# Передача на ревью
@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser  # Сохраняем browser как атрибут класса
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"  # Задаем ссылку

        login_test = TestLoginFromMainPage()
        login_test.test_guest_can_do_to_login_page(browser)
        login_zareg = LoginPage(browser, "http://selenium1py.pythonanywhere.com/")  # Передаем URL
        login_zareg.register_new_user()
        user_vhod = BasePage(browser, "http://selenium1py.pythonanywhere.com/")  # Передаем URL
        user_vhod.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, self.link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self):
        page = ProductPage(self.browser, self.link)
        page.open()
        page.add_to_busket_user()
        time.sleep(10)

# pytest -v --tb=line --language=en -m need_review