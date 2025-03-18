from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ProductPage наследует класс BasePage, может использовать все методы класса BasePage
class ProductPage(BasePage): 
    
    # Функция клиякает по кнопке Добавления
    def add_to_busket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        self.solve_quiz_and_get_code()

     # Функция получает название товара
    def get_product_name(self):
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return name_product.text
    
     # Функция получает цену товара
    def get_product_price(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return price_product.text
    
    # Функция сравенеия названия в карточке товара и названия в поле корзины
    def sravnenie_name(self):
        
        # Вызываем функция нажатия на кнопку корзины
        self.add_to_busket()

        # Присваиваем объект имени карточки товара из функции get_product_name()
        name_product_book = self.get_product_name()

        # Присваиваем объект имени поля корзины. Сначала находим и переводим в текст.
        busket_name = self.browser.find_element(*ProductPageLocators.BUSKET_PRODUCT_NAME).text

        print(f"Название книги на странице: {name_product_book}")
        print(f"Название книги в корзине: {busket_name}")
        # Сравниваем
        assert name_product_book in busket_name, f"Название книги в добавлении: {busket_name} не совпадает с заголовком: {name_product_book}"

    #  Функция сравенеия цены в карточке товара и цены в поле корзины
    def sravnenie_price(self):
        
        self.add_to_busket()

        price_product_book = self.get_product_price()
    
        busket_price = self.browser.find_element(*ProductPageLocators.BUSKET_PRODUCT_PRICE).text

        print(f"Цена книги на странице: {price_product_book}")
        print(f"Цена книги в корзине: {busket_price}")
        assert price_product_book == busket_price, f"Цена книги в добавлении: {busket_price} не совпадает с заголовком: {price_product_book}"

    def sravnenie_oba(self):
        self.add_to_busket()

        price_product_book = self.get_product_price()
        name_product_book = self.get_product_name()
        
        busket_price = self.browser.find_element(*ProductPageLocators.BUSKET_PRODUCT_PRICE).text
        busket_name = self.browser.find_element(*ProductPageLocators.BUSKET_PRODUCT_NAME).text

        print(f"Цена книги и цены на странице: {price_product_book} и {name_product_book}")
        print(f"Цена книги и цены в корзине: {busket_price} и {busket_name}")
        
        assert price_product_book == busket_price, f"Цена книги в добавлении: {busket_price} не совпадает с заголовком и ценой: {price_product_book}"

        assert name_product_book == busket_name, f"Название книги в добавлении: {busket_name} не совпадает с заголовком и ценой: {name_product_book}"
