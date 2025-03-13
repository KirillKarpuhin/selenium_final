import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser): 
   browser.get(link) 
   go_to_login_page(browser) 

#def test_add_to_cart(browser):
 #   page = ProductPage(url="", browser)   # инициализируем объект Page Object
  #  page.open()                           # открываем страницу в браузере
  #  page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
  #   page.add_product_to_cart()            # жмем кнопку добавить в корзину 
   #    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом

# pytest -v --tb=line --language=en test_main_page.py
# PyTest --tb=line, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста