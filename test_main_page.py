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

# объединим в группу два теста в файле и пометим его меткой login_gues

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_do_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link) #  инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                    # открываем страницу
        page.go_to_login_page()        # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()





#def test_add_to_cart(browser):
 #   page = ProductPage(url="", browser)   # инициализируем объект Page Object
  #  page.open()                           # открываем страницу в браузере
  #  page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
  #   page.add_product_to_cart()            # жмем кнопку добавить в корзину 
   #    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом

# pytest -v --tb=line --language=en test_main_page.py
# PyTest --tb=line, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста

# pytest -v -s --tb=line --language=en test_main_page.py