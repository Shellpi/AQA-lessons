"""Homework 13_1."""

import csv
import os

import requests

"""
Task 1.

Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на
наявність дублікатів і приберіть їх. Результат запишіть у
файл result_<your_second_name>.csv
"""

TASK_START_TEMPLATE = '\n---Task {0}---\n'
print(TASK_START_TEMPLATE.format('01'))


def download_file(url, local_path):
    """Download RAW files from URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Checks for mistakes
        with open(local_path, 'wb') as file:
            file.write(response.content)
    except requests.exceptions.Timeout:
        print(f'Request to {url} timed out.')
    except requests.exceptions.RequestException as err:
        print(f'An error occurred: {err}')


def csv_duplicate_remover(file1_url, file2_url, result_file):
    """Download and remove duplicates from 2 csv files."""
    # File downloading
    file1 = 'file1.csv'
    file2 = 'file2.csv'
    download_file(file1_url, file1)
    download_file(file2_url, file2)

    try:
        with open(file1, mode='r', newline='', encoding='utf-8') as f1:
            reader1 = csv.reader(f1)

            # Check if the file is empty
            first_row = next(reader1, None)
            if not first_row:
                raise ValueError('The CSV file is empty.')
            data1 = list(reader1)

        with open(file2, mode='r', newline='', encoding='utf-8') as f2:
            reader2 = csv.reader(f2)

            # Check if the file is empty
            first_row = next(reader2, None)
            if not first_row:
                raise ValueError('The CSV file is empty.')
            data2 = list(reader2)

        # Collect all data from both files.
        all_data = data1 + data2
        # Duplicate removing.
        unique_data = [list(line)
                       for line in {tuple(row) for row in all_data}]

        with (open(result_file, mode='w', newline='', encoding='utf-8')
              as result):
            surname = csv.writer(result)
            surname.writerow(unique_data)

        return f'Duplicates has been removed. Check the file {result_file}'

    finally:
        # Delete the downloaded files
        if os.path.exists(file1):
            os.remove(file1)
        if os.path.exists(file2):
            os.remove(file2)


# URLs to raw CSV files on GitHub
f1_url = ('https://raw.githubusercontent.com/dntpanix/automation_qa/main'
          '/ideas_for_test/work_with_csv/random.csv')
f2_url = ('https://raw.githubusercontent.com/dntpanix/automation_qa/main'
          '/ideas_for_test/work_with_csv/random-michaels.csv')
csv3 = 'result_Putintsev.csv'

print(csv_duplicate_remover(f1_url, f2_url, csv3))
