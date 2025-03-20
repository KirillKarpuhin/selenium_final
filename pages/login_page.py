from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        assert self.browser.current_url.count('login') != 0, 'Подстроки login нет в текущем url браузера'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина отсутствует на странице"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации отсутствует на странице"

    def register_new_user(self):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email = str(time.time()) + "@fakemail.org"
        email_form.send_keys(email)

        password_form = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password = "password11..2"
        password_form.send_keys(password)

        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        confirm_password.send_keys(password)

        confirm_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        confirm_button.click()