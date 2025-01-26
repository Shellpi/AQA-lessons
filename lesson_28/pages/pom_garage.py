"""Page Object Model for Garage page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import GARAGE_PAGE_LOCATORS

class GaragePage:
    """Page Object Model for Garage page."""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, timeout, locator, condition=EC.visibility_of_element_located):
        """Ждет элемента с указанным условием."""
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def logout_click_dropdown(self, timeout):
        """Выход через выпадающее меню."""
        dropdown_logout = self.wait_for_element(timeout, GARAGE_PAGE_LOCATORS['dropdown_log_out_button'])
        dropdown_logout.click()

    def logout_click_menu(self, timeout):
        """Выход через боковую панель."""
        menu_logout = self.wait_for_element(timeout, GARAGE_PAGE_LOCATORS['menu_log_out_button'])
        menu_logout.click()
