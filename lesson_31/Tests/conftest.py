import pytest
import logging
from logging.handlers import RotatingFileHandler
from selenium import webdriver
import os
import subprocess

base_url = 'https://tracking.novaposhta.ua/#/uk'
drivers = {
    'Chrome': webdriver.Chrome,
    'Firefox': webdriver.Firefox,
}

# Logger setup
@pytest.fixture(scope='session', autouse=True)
def test_logger():
    """Logger setup."""
    logger = logging.getLogger('Main')
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    rotating_handler = RotatingFileHandler(
        filename='logs.log', mode='a', maxBytes=10000, backupCount=3, encoding='utf-8'
    )
    rotating_handler.setLevel(logging.INFO)
    rotating_handler.setFormatter(formatter)

    logger.handlers = [console_handler, rotating_handler]
    return logger

# WebDriver setup
@pytest.fixture(params=drivers.keys(), scope='class')
def driver(request):
    """WebDriver setup."""
    browser_name = request.param
    try:
        driver = drivers[browser_name]()
        driver.get(base_url)
        yield driver
    except Exception as e:
        pytest.fail(f"Error initializing {browser_name} driver: {e}")
    finally:
        driver.quit()
