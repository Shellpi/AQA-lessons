"""Page Object Model for Sign In page."""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SIGN_IN_LOCATORS, SIGN_UP_LOCATORS, SIGN_UP_ERROR_LOCATORS

class SignIn:
    """Page Object Model for Sign In page."""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, timeout, locator, condition=EC.visibility_of_element_located):
        """Ждет элемента с указанным условием."""
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def click_element(self, timeout, locator):
        """Ожидает и кликает по элементу."""
        element = self.wait_for_element(timeout, locator, EC.element_to_be_clickable)
        element.click()

    def fill_field(self, locator, value, timeout=5):
        """Ожидает и заполняет поле значением."""
        field_element = self.wait_for_element(timeout, locator)
        field_element.clear()
        field_element.send_keys(value)

    def fill_the_login_form(self, email, password, timeout=5):
        """Заполняет форму логина."""
        self.fill_field(SIGN_IN_LOCATORS['email_textfield'], email, timeout)
        self.fill_field(SIGN_IN_LOCATORS['password_textfield'], password, timeout)

    def registration_through_sign_in_button(self, timeout):
        """Открывает окно регистрации через кнопку Sign In."""
        self.click_element(timeout, SIGN_IN_LOCATORS['sign_in_button'])
        self.click_element(timeout, SIGN_IN_LOCATORS['registration_login_button'])
