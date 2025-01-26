"""Page Object Model for Sign In page."""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SIGN_IN_LOCATORS, SIGN_UP_LOCATORS, SIGN_UP_ERROR_LOCATORS

class SignIn:
    """Page Object Model for Sign In page."""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, timeout, locator, condition=EC.visibility_of_element_located):
        """Waits for the element with condition."""
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def click_element(self, timeout, locator):
        """Waits and click for the element."""
        element = self.wait_for_element(timeout, locator, EC.element_to_be_clickable)
        element.click()

    def fill_field(self, locator, value, timeout=5):
        """Fills the element fields."""
        field_element = self.wait_for_element(timeout, locator)
        field_element.clear()
        field_element.send_keys(value)

    def fill_the_login_form(self, email, password, timeout=5):
        """Fills the login form."""
        self.fill_field(SIGN_IN_LOCATORS['email_textfield'], email, timeout)
        self.fill_field(SIGN_IN_LOCATORS['password_textfield'], password, timeout)

    def registration_through_sign_in_button(self, timeout):
        """Opens the Sign In registration window."""
        self.click_element(timeout, SIGN_IN_LOCATORS['sign_in_button'])
        self.click_element(timeout, SIGN_IN_LOCATORS['registration_login_button'])
