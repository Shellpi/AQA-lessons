"""Homework 13_2."""

import json
import logging
import os

import requests

"""
Task 2.

Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json
є валідними json.
Результат для невалідного файлу виведіть через логер на рівні еррор
у файл json__<your_second_name>.log
"""

TASK_START_TEMPLATE = '\n---Task {0}---\n'
print(TASK_START_TEMPLATE.format('02'))


def logger_setup():
    """Set up a logger for error handling."""
    logger = logging.getLogger('Main')
    logger.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(filename='json__Putintsev.log',
                                       mode='w', encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


def file_downloader(url, local_path, logger):
    """Download a file from a URL and save it locally."""
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        with open(local_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    except requests.RequestException as err:
        logger.error(f'Failed to download {url}: {err}')
        raise


def json_valid_checker(urls, logger):
    """Check JSON validity of downloaded files."""
    downloaded_files = []
    invalid_files = []

    try:
        for url in urls:
            file_name = os.path.basename(url)  # Get the file name
            try:
                file_downloader(url, file_name, logger)
                downloaded_files.append(file_name)
            except Exception as err:
                logger.error(f'Error downloading {url}: {err}')
                continue

        for json_file in downloaded_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as json_fh:
                    json.load(json_fh)
            except json.decoder.JSONDecodeError as j_err:
                logger.error(f'Invalid JSON {json_file}: {j_err}')
                invalid_files.append(json_file)

    finally:
        # Remove our files.
        for json_file in downloaded_files:
            if os.path.exists(json_file):
                os.remove(json_file)

    return f'Invalid: {invalid_files}' if invalid_files else 'Files are valid.'


if __name__ == '__main__':
    logger = logger_setup()
    urls = [
        'https://raw.githubusercontent.com/dntpanix/automation_qa/refs'
        '/heads/main/ideas_for_test/work_with_json/localizations_en.json',
        'https://raw.githubusercontent.com/dntpanix/automation_qa/refs'
        '/heads/main/ideas_for_test/work_with_json/localizations_ru.json',
        'https://raw.githubusercontent.com/dntpanix/automation_qa/refs'
        '/heads/main/ideas_for_test/work_with_json/login.json',
        'https://raw.githubusercontent.com/dntpanix/automation_qa/refs'
        '/heads/main/ideas_for_test/work_with_json/swagger.json',
    ]
    result = json_valid_checker(urls, logger)
    print(result)
