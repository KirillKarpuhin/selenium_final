from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_busket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        self.solve_quiz_and_get_code()