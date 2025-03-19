import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from .locators import MainPageLocators
from .login_page import LoginPage
import time
import math
# импорт базового класса BasePage из файла base.page
from .base_page import BasePage

# MainPage наследник класса BasePage. Таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка. 

class MainPage(BasePage): 
   pass # заглушка