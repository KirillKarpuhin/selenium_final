from selenium.webdriver.common.by import By

# Пара внешней переменной: теперь каждый селектор — это пара: как искать и что искать. 
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():

    # Нажатие на кнопку Добавления
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Локаторы поиска имени\цены в карточке товара
    PRODUCT_NAME = (By.CSS_SELECTOR,"div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,"p.price_color")

    # Локаторы поиска имени\цены в поле добавления
    BUSKET_PRODUCT_NAME = (By.CSS_SELECTOR,".alertinner strong")
    BUSKET_PRODUCT_PRICE = (By.CSS_SELECTOR, "[class='alert alert-safe alert-noicon alert-info  fade in'] strong")


    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success")
    PRODUCT_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success > .alertinner > strong")
    TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner > p > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")