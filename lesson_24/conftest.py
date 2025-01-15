"""Setup for tests."""

import logging
from logging.handlers import RotatingFileHandler

import pytest
import requests
from requests.auth import HTTPBasicAuth

base_url = 'http://127.0.0.1:8080'
username = 'Vlad'
password = 'test_123'

@pytest.fixture(scope='session', autouse=True)
def test_logger():
    """Logger setup."""
    logger = logging.getLogger('Main')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console settings
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # Rotating file handler settings
    rotating_handler = RotatingFileHandler(filename='test_search.log', mode='a', maxBytes=10000, backupCount=5)
    rotating_handler.setLevel(logging.INFO)
    rotating_handler.setFormatter(formatter)

    logger.handlers = [console_handler, rotating_handler]

    return logger

@pytest.fixture(scope='class')
def auth_process():
    """Fixture to authenticate and provide access."""
    session = None
    try:
        # Auth request
        response = requests.post(f'{base_url}/auth', auth=HTTPBasicAuth(username, password), timeout=5)
        response.raise_for_status()

        # Token response
        token = response.json()['access_token']
        session = requests.Session()
        session.headers.update({'Authorization': f'Bearer {token}'})

        yield session

    except requests.exceptions.RequestException as err:
        pytest.fail(f"Request error occurred: {err}", pytrace=True)
    except Exception as exc:
        pytest.fail(f"Unexpected error occurred: {exc}", pytrace=True)
    finally:
        if session is not None:
            session.close()
