"""Optimized conftest.py and test_homework27.py."""

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
        'search_button_enabled': (By.CLASS_NAME, 'track__form-group-btn.green-active'),
        'error_message': (By.XPATH, "//div[@id='np-number-input-desktop-message-error-message']/span"),
        'package_status': (By.CLASS_NAME, 'header__status-text'),
    }

    def __init__(self, driver, logger):
        """Initialize driver and logger."""
        self.driver = driver
        self.logger = logger

    def clear_and_type(self, locator, text):
        """Clear and type."""
        field = self.driver.find_element(*locator)
        field.clear()
        field.send_keys(text)

    def get_element_text(self, locator):
        """Get element text."""
        return self.driver.find_element(*locator).text

    def wait_for_element(self, locator):
        """Wait for element."""
        return WebDriverWait(self.driver, ELEMENT_WAIT_TIMEOUT).until(
            EC.visibility_of_element_located(locator),
        )

    def button_disabled(self):
        """Verify disabled button."""
        self.driver.find_element(*self.LOCATORS['text_input_field']).clear()
        assert self.driver.find_element(*self.LOCATORS['search_button_disabled']).is_displayed(), \
            'Disabled button is not displayed.'

    def button_enabled(self, track_num):
        """Verify enabled button."""
        self.clear_and_type(self.LOCATORS['text_input_field'], track_num)
        assert self.driver.find_element(*self.LOCATORS['search_button_enabled']).is_displayed(), \
            'Enabled button is not displayed.'

    def get_error_message(self, bad_track_num):
        """Retrieve error message for invalid tracking number."""
        try:
            self.clear_and_type(self.LOCATORS['text_input_field'], bad_track_num)
            self.driver.find_element(*self.LOCATORS['search_button_enabled']).click()
            error_element = self.wait_for_element(self.LOCATORS['error_message'])
            return error_element.text
        except Exception as e:
            self.logger.error(f'Error retrieving error message: {e}')
            pytest.fail(f'Error retrieving error message: {e}')

    def get_tracking_info(self, track_num):
        """Retrieve tracking information for a valid tracking number."""
        try:
            self.clear_and_type(self.LOCATORS['text_input_field'], track_num)
            self.driver.find_element(*self.LOCATORS['search_button_enabled']).click()
            status_element = self.wait_for_element(self.LOCATORS['package_status'])
            return status_element.text
        except Exception as e:
            self.logger.error(f'Error retrieving tracking info: {e}')
            pytest.fail(f'Error retrieving tracking info: {e}')


@pytest.mark.parametrize('track_num, bad_track_num, expected_message', [
    (DEFAULT_TRACK_NUM, DEFAULT_BAD_TRACK_NUM, EXPECTED_ERR_MESSAGE),
])
def test_search_page(driver, test_logger, track_num, bad_track_num, expected_message):
    """Tests for the search page."""
    search_page = SearchPage(driver, test_logger)

    # Verify disabled button
    search_page.button_disabled()

    # Verify enabled button
    search_page.button_enabled(track_num)

    # Verify error message
    actual_message = search_page.get_error_message(bad_track_num)
    assert actual_message == expected_message, \
        f"Expected '{expected_message}', but got '{actual_message}'"

    # Verify tracking info
    status = search_page.get_tracking_info(track_num)
    test_logger.info(f'Tracking status: {status}')
