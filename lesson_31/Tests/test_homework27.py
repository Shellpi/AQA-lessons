import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Configuration
BASE_URL = 'https://tracking.novaposhta.ua/#/uk'
DRIVERS = {
    'Chrome': webdriver.Chrome,
    'Firefox': webdriver.Firefox,
}
ELEMENT_WAIT_TIMEOUT = 5
DEFAULT_TRACK_NUM = '20451073763641'
DEFAULT_BAD_TRACK_NUM = '2045107376364'
EXPECTED_ERR_MESSAGE = (
    'Ми не знайшли посилку за таким номером. '
    'Якщо ви шукаєте інформацію про посилку, якій більше 3 місяців, '
    'будь ласка, зверніться у контакт-центр: 0 800 500 609'
)


class SearchPage:
    """Page object model for the Search Page."""

    LOCATORS = {
        'text_input_field': (By.ID, 'en'),
        'search_button_disabled': (By.CLASS_NAME, 'track__form-group-btn'),
        'search_button_enabled': (By.CSS_SELECTOR, '.track__form-group-btn.green-active'),
        'error_message': (By.XPATH, "//div[@id='np-number-input-desktop-message-error-message']/span"),
        'package_status': (By.CLASS_NAME, 'header__status-text'),
    }

    def __init__(self, driver, logger):
        """Initialize driver and logger."""
        self.driver = driver
        self.logger = logger

    @allure.step("Clear and type text into the field")
    def clear_and_type(self, locator, text):
        """Clear and type."""
        field = self.driver.find_element(*locator)
        field.clear()
        field.send_keys(text)

    @allure.step("Get element text")
    def get_element_text(self, locator):
        """Get element text."""
        return self.driver.find_element(*locator).text

    @allure.step("Wait for element to be visible")
    def wait_for_element(self, locator):
        """Wait for element."""
        return WebDriverWait(self.driver, ELEMENT_WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(locator),
        )

    @allure.step("Verify that the button is disabled")
    def button_disabled(self):
        """Verify disabled button."""
        self.driver.find_element(*self.LOCATORS['text_input_field']).clear()
        assert not self.driver.find_element(*self.LOCATORS['search_button_disabled']).is_enabled(), \
            'Button should be disabled but is enabled.'

    @allure.step("Verify that the button is enabled")
    def button_enabled(self, track_num):
        """Verify enabled button."""
        self.clear_and_type(self.LOCATORS['text_input_field'], track_num)
        assert self.driver.find_element(*self.LOCATORS['search_button_enabled']).is_enabled(), \
            'Button should be enabled but is disabled.'

    @allure.step("Get error message for invalid tracking number")
    def get_error_message(self, bad_track_num):
        """Retrieve error message for invalid tracking number."""
        try:
            self.clear_and_type(self.LOCATORS['text_input_field'], bad_track_num)
            search_button = self.driver.find_element(*self.LOCATORS['search_button_enabled'])
            assert search_button.is_enabled(), 'Search button is not enabled.'
            search_button.click()
            error_element = self.wait_for_element(self.LOCATORS['error_message'])
            return error_element.text
        except Exception as e:
            self.logger.error(f'Error retrieving error message: {e}')
            pytest.fail(f'Error retrieving error message: {e}')

    @allure.step("Get tracking information for a valid tracking number")
    def get_tracking_info(self, track_num):
        """Retrieve tracking information for a valid tracking number."""
        try:
            self.clear_and_type(self.LOCATORS['text_input_field'], track_num)
            search_button = self.driver.find_element(*self.LOCATORS['search_button_enabled'])
            assert search_button.is_enabled(), 'Search button is not enabled.'
            search_button.click()
            status_element = self.wait_for_element(self.LOCATORS['package_status'])
            return status_element.text
        except Exception as e:
            self.logger.error(f'Error retrieving tracking info: {e}')
            pytest.fail(f'Error retrieving tracking info: {e}')


@allure.feature("Button State")
def test_button_state(driver, test_logger):
    """Test button state (disabled/enabled)."""
    search_page = SearchPage(driver, test_logger)

    with allure.step("Verify that the button is disabled when the input field is empty"):
        search_page.button_disabled()

    with allure.step("Verify that the button is enabled when a valid tracking number is entered"):
        search_page.button_enabled(DEFAULT_TRACK_NUM)


@allure.feature("Error Handling")
def test_error_message(driver, test_logger):
    """Test error message for invalid tracking number."""
    search_page = SearchPage(driver, test_logger)

    with allure.step("Verify error message for invalid tracking number"):
        actual_message = search_page.get_error_message(DEFAULT_BAD_TRACK_NUM)
        assert actual_message == EXPECTED_ERR_MESSAGE, \
            f"Expected '{EXPECTED_ERR_MESSAGE}', but got '{actual_message}'"


@allure.feature("Tracking Information")
def test_tracking_info(driver, test_logger):
    """Test tracking information for a valid tracking number."""
    search_page = SearchPage(driver, test_logger)

    with allure.step("Verify tracking information for a valid tracking number"):
        status = search_page.get_tracking_info(DEFAULT_TRACK_NUM)
        test_logger.info(f'Tracking status: {status}')
