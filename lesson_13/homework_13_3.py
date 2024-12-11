"""Homework 13_3."""

import logging
import os

import requests
from lxml import etree

"""
Task 3.

Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по
group/number і повернення значення timingExbytes/incoming результат виведіть
у консоль через логер на рівні інфо
"""

TASK_START_TEMPLATE = '\n---Task {0}---\n'
print(TASK_START_TEMPLATE.format('03'))


def logger_setup():
    """Set up a logger."""
    logger = logging.getLogger('Main')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


def download_file(url, local_path):
    """Download RAW file from URL."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    with open(local_path, 'wb') as file:
        file.write(response.content)


def delete_file(file_path):
    """Delete a file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)


def find_timing_incoming(file_url, group_number, logger):
    """Find the timingExbytes/incoming value for the selected group."""
    file = 'file.xml'

    try:
        download_file(file_url, file)
        tree = etree.parse(file)
        root = tree.getroot()
        groups = root.findall('group')
        group_numbers = [int(group.find('number').text) for group in groups
                         if group.find('number') is not None]

        if group_number not in group_numbers:
            logger.info(f'The group {group_number} does not exist.')
            return

        for group in groups:
            number = int(group.find('number').text)
            if number == group_number:
                incoming_value = group.find('./timingExbytes/incoming')
                if incoming_value is not None:
                    logger.info(f'The timingExbytes/incoming value for group '
                                f'{number} is: {incoming_value.text}')
                else:
                    logger.info(f'No timingExbytes/incoming value found '
                                f'for group {number}.')
                break

    except Exception as err:
        logger.error(f'An error has been found: {err}')

    finally:
        delete_file(file)


if __name__ == '__main__':
    logger = logger_setup()
    file_url = ('https://raw.githubusercontent.com/dntpanix/automation_qa/refs'
                '/heads/main/ideas_for_test/work_with_xml/groups.xml')
    selected_group = 2
    find_timing_incoming(file_url, selected_group, logger)
