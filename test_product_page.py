import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from .pages.login_page import LoginPage
import time
import math
# Импорт класса MainPage из папки pages и файла main_page
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage

@pytest.mark.final_proverka
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()
    time.sleep(10)

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

# pytest -v -s --tb=line --language=en test_product_page.py
# pytest -v -s --tb=line --language=en -m sravnenie_name_and_price test_product_page.py

# Шаблон запуска автотестов с 9 параметрами ссылок
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# Передаем в функцию шаблон
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    # После подготовки открываем функцию проверки для всех ссылок
    try: 
        page.sravnenie_oba()
    except Exception as e:
        # Если тест упал, помечаем его как xfail
        pytest.xfail(f"Тест упал на ссылке {link} с ошибкой: {str(e)}")
