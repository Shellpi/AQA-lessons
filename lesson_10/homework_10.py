"""Homework 11.

Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування
подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
from logging.handlers import RotatingFileHandler

# Logger settings
logger = logging.getLogger('log_event')
logger.setLevel(logging.INFO)

# Rotating handler
rotating_handler = RotatingFileHandler(
    filename='login_system.log',
    mode='a',
    maxBytes=10000,
    backupCount=5,
)
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
rotating_handler.setFormatter(log_formatter)
logger.addHandler(rotating_handler)


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити,
    логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f'Login event - Username: {username}, Status: {status}'

    # Логування події
    if status == 'success':
        logger.info(log_message)
    elif status == 'expired':
        logger.warning(log_message)
    else:
        logger.error(log_message)
