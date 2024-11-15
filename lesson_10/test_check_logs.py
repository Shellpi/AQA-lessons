"""Tests for checking logs with login actions and errors."""

import logging

from homework_10 import log_event

LOG_FILE = 'login_system.log'
logger = logging.getLogger('log_event')


def test_log_success_event():
    """Test for successful login with INFO log."""
    log_event('user123', 'success')
    with open(LOG_FILE, 'r') as log_file:
        log_content = log_file.read()
    assert ('INFO - Login event - Username: user123, Status: success'
            in log_content)


def test_log_expired_event():
    """Test for expired PW with Expired log status."""
    log_event('user123', 'expired')
    with open(LOG_FILE, 'r') as log_file:
        log_content = log_file.read()
    assert ('WARNING - Login event - Username: user123, Status: expired'
            in log_content)


def test_log_failed_event():
    """Test for failed login with Failed log status."""
    log_event('user123', 'failed')
    with open(LOG_FILE, 'r') as log_file:
        log_content = log_file.read()
    assert ('ERROR - Login event - Username: user123, Status: failed'
            in log_content)


def test_log_unknown_event():
    """Test for login with unknown status."""
    log_event('user123', 'unknown_status')
    with open(LOG_FILE, 'r') as log_file:
        log_content = log_file.read()
    assert ('ERROR - Login event - Username: user123, Status: unknown_status'
            in log_content)
