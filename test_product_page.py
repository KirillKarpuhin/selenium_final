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
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()