import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
# импорт базового класса BasePage из файла base.page
from .base_page import BasePage

# MainPage наследник класса BasePage. Таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка. 
class MainPage(BasePage):
    #  go_to_login_page(self) передается экземпляр браузера из BasePage. Атрбудт self доступ к атрибутам и методам класса BP
    def go_to_login_page(self):
        # self.browser обращается так же как аргумент класса BasePage
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
