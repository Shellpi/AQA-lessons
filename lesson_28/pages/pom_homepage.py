"""Page Object Model for Home page with guest button."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HOME_PAGE_LOCATORS

class HomePage:
    """Page Object Model for Home page."""

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, timeout, locator, condition=EC.visibility_of_element_located):
        """Ждет элемента с указанным условием."""
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def click_element(self, timeout, locator):
        """Ожидает и кликает по элементу."""
        element = self.wait_for_element(timeout, locator, EC.element_to_be_clickable)
        element.click()

    def login_as_guest(self, timeout):
        """Вход в систему как гость."""
        self.click_element(timeout, HOME_PAGE_LOCATORS['guest_log_in_button'])

    def logout_via_menu(self, timeout, garage_page):
        """Выход через боковую панель."""
        garage_page.logout_click_menu(timeout)

    def logout_via_dropdown(self, timeout, garage_page):
        """Выход через выпадающее меню."""
        self.click_element(timeout, HOME_PAGE_LOCATORS['guest_log_in_button'])
        self.click_element(timeout, HOME_PAGE_LOCATORS['menu_dropdown_button'])
        garage_page.logout_click_dropdown(timeout)
