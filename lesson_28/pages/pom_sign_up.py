"""Page Object Model for Sign Up page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SIGN_UP_LOCATORS, SIGN_UP_ERROR_LOCATORS

class SignUp:
    """Page Object Model for Sign Up page."""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, timeout, locator, condition=EC.visibility_of_element_located):
        """Ждет элемента с указанным условием."""
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def click_element(self, timeout, locator):
        """Ожидает и кликает по элементу."""
        element = self.wait_for_element(timeout, locator, EC.element_to_be_clickable)
        element.click()

    def fill_field(self, field_name, value):
        """Заполняет поле в форме регистрации."""
        locator = SIGN_UP_LOCATORS[field_name]
        field_element = self.wait_for_element(5, locator)
        field_element.clear()
        field_element.send_keys(value)

    def fill_form(self, name, last_name, email, password, re_password):
        """Заполняет форму регистрации."""
        self.fill_field('name', name)
        self.fill_field('last_name', last_name)
        self.fill_field('email', email)
        self.fill_field('password', password)
        self.fill_field('confirm', re_password)
