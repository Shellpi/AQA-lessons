"""Hometask 28."""

import random

import pytest
from locators import (HOME_PAGE_LOCATORS, SIGN_IN_ERROR_LOCATORS,
                      SIGN_IN_LOCATORS, SIGN_IN_SUCCESS_LOCATORS,
                      SIGN_UP_ERROR_LOCATORS, SIGN_UP_LOCATORS)
from pages.pom_garage import GaragePage
from pages.pom_homepage import HomePage
from pages.pom_sign_in import SignIn
from pages.pom_sign_up import SignUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Configuration
BASE_URL = 'https://guest:welcome2qauto@qauto2.forstudy.space'
ELEMENT_WAIT_TIMEOUT = 5

# Test data
NAME = 'Adam'
LAST_NAME = 'Smith'
PASSWORD = 'Test123123'
BAD_PASSWORD = '123'
MISMATCH_PASSWORD = 'Test321321'
EMAIL = f'Test+{random.randint(1000, 5555)}@google.com'


def test_login_with_guest_acc(driver):
    """Test for logging in and out as a guest."""
    home_page = HomePage(driver)
    garage_page = GaragePage(driver)
    home_page.login_as_guest(ELEMENT_WAIT_TIMEOUT)
    home_page.logout_via_menu(ELEMENT_WAIT_TIMEOUT, garage_page)
    home_page.logout_via_dropdown(ELEMENT_WAIT_TIMEOUT, garage_page)


@pytest.mark.parametrize(
    'name, last_name, email, password, re_password, expected_message',
    [
        ('', LAST_NAME, EMAIL, PASSWORD, PASSWORD, 'Name required'),
        ('A', LAST_NAME, EMAIL, PASSWORD, PASSWORD,
         'Name has to be from 2 to 20 characters long'),
        (NAME, '', EMAIL, PASSWORD, PASSWORD, 'Last name required'),
        (NAME, 'B', EMAIL, PASSWORD, PASSWORD,
         'Last name has to be from 2 to 20 characters long'),
        (NAME, LAST_NAME, '', PASSWORD, PASSWORD, 'Email required'),
        (NAME, LAST_NAME, 'Test123', PASSWORD, PASSWORD, 'Email is incorrect'),
        (NAME, LAST_NAME, EMAIL, '', PASSWORD, 'Password required'),
        (NAME, LAST_NAME, EMAIL, '123', PASSWORD,
         'Password has to be from 8 to 15 characters long and contain '
         'at least one integer, one capital, and one small letter'),
        (NAME, LAST_NAME, EMAIL, PASSWORD, '', 'Re-enter password required'),
        (NAME, LAST_NAME, EMAIL, BAD_PASSWORD, BAD_PASSWORD,
         'Password has to be from 8 to 15 characters long and contain at '
         'least one integer, one capital, and one small letter'),
        (NAME, LAST_NAME, EMAIL, PASSWORD, MISMATCH_PASSWORD,
         'Passwords do not match'),
        (NAME, LAST_NAME, EMAIL, PASSWORD, PASSWORD, 'Registration complete'),
    ],
)
def test_registration_through_sign_in_window(driver,
                                             name, last_name, email,
                                             password, re_password,
                                             expected_message, test_logger):
    """Tests registration."""
    sign_up_page = SignUp(driver)
    sign_in_page = SignIn(driver)

    test_logger.info('The registration window opens.')
    sign_in_page.registration_through_sign_in_button(ELEMENT_WAIT_TIMEOUT)

    test_logger.info('Registration fields filling with data.')
    sign_up_page.fill_form(name, last_name, email, password, re_password)

    register_button = sign_up_page.wait_for_element(
        ELEMENT_WAIT_TIMEOUT, SIGN_UP_LOCATORS['register_button'],
    )
    register_button.click()

    test_logger.info('Waiting for the message (success / fail)')

    # Success locator
    success_locator = SIGN_UP_LOCATORS['success_message']

    # Error locator
    error_locator = SIGN_UP_ERROR_LOCATORS.get(expected_message)

    try:
        if expected_message == 'Registration complete':
            message_element = WebDriverWait(driver,
                                            ELEMENT_WAIT_TIMEOUT).until(
                EC.visibility_of_element_located(success_locator),
            )
        else:
            if error_locator is None:
                test_logger.error(f"Key '{expected_message}'"
                                  f' is missing in the ERROR_LOCATORS')
                pytest.fail(f"Key '{expected_message}'"
                            f' is missing in the ERROR_LOCATORS')

            message_element = WebDriverWait(driver,
                                            ELEMENT_WAIT_TIMEOUT).until(
                EC.visibility_of_element_located(error_locator),
            )

        actual_message = message_element.text
        test_logger.info(f'The message: {actual_message}')
    except Exception as e:
        test_logger.error(f'The message is missing: {e}')
        pytest.fail(f'The message is missing: {e}')

    test_logger.info(f'Compare actual with '
                     f'expected: '
                     f'{actual_message} == {expected_message}')
    assert actual_message == expected_message, (f'Expected: '
                                                f'{expected_message}, '
                                                f'but got: {actual_message}')


@pytest.mark.parametrize(
    'email, password, expected_message',
    [
        ('', PASSWORD, 'Email required'),
        ('Test', PASSWORD, 'Email is incorrect'),
        (EMAIL, '', 'Password required'),
        (EMAIL, MISMATCH_PASSWORD, 'Wrong email or password'),
        (EMAIL, PASSWORD, 'You have been successfully logged in'),
    ],
)
def test_sign_in(driver, email, password, expected_message, test_logger):
    """Sign in tests."""
    home_page = HomePage(driver)
    sign_in_page = SignIn(driver)

    test_logger.info('Opens the login window')
    home_page.click_element(ELEMENT_WAIT_TIMEOUT,
                            HOME_PAGE_LOCATORS['sign_in_button'])

    test_logger.info('Fills login fields')
    sign_in_page.fill_the_login_form(email, password)

    login_button = sign_in_page.wait_for_element(
        ELEMENT_WAIT_TIMEOUT, SIGN_IN_LOCATORS['login_button'],
    )
    login_button.click()

    test_logger.info('Waiting for the message (success / fail)')


    success_locator = SIGN_IN_SUCCESS_LOCATORS['login_success_message']

    error_locator = SIGN_IN_ERROR_LOCATORS.get(expected_message)

    try:
        if expected_message == 'You have been successfully logged in':
            message_element = WebDriverWait(driver, ELEMENT_WAIT_TIMEOUT).until(
                EC.visibility_of_element_located(success_locator),
            )
        else:
            if error_locator is None:
                test_logger.error(f"The key '{expected_message}'"
                                  f' is missing in the ERROR_LOCATORS')
                pytest.fail(f"The key '{expected_message}'"
                            f' is missing in the ERROR_LOCATORS')

            message_element = WebDriverWait(driver, ELEMENT_WAIT_TIMEOUT).until(
                EC.visibility_of_element_located(error_locator),
            )

        actual_message = message_element.text
        test_logger.info(f'Message found: {actual_message}')
    except Exception as e:
        test_logger.error(f'Message is missing: {e}')
        pytest.fail(f'Message is missing: {e}')

    test_logger.info(f'Compare actual with '
                     f'expected: {actual_message} == {expected_message}')
    assert actual_message == expected_message, (f'Expected: {expected_message}'
                                                f', but got: {actual_message}')
