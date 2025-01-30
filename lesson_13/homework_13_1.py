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


def read_csv_file(file_path):
    """Read a CSV file and return its data as a list of rows."""
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        # Check if the file is empty
        first_row = next(reader, None)
        if not first_row:
            raise ValueError(f'The CSV file "{file_path}" is empty.')

        # Return the rest of the file as a list of rows
        return [first_row] + list(reader)


def delete_file(file_path):
    """Delete a file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)


def csv_duplicate_remover(file1_url, file2_url, result_file):
    """Download and remove duplicates from 2 csv files."""
    # File downloading
    file1 = 'file1.csv'
    file2 = 'file2.csv'
    download_file(file1_url, file1)
    download_file(file2_url, file2)

    try:
        # Read data from both files using the helper function
        data1 = read_csv_file(file1)
        data2 = read_csv_file(file2)

        # Collect all data from both files.
        all_data = data1 + data2

        # Remove duplicates.
        unique_data = [list(line) for line in {tuple(row) for row in all_data}]

        # Write the unique data to the result file
        with open(result_file, mode='w', newline='', encoding='utf-8') as res:
            writer = csv.writer(res)
            writer.writerows(unique_data)

        return f'Duplicates have been removed. Check the file "{result_file}".'

    finally:
        delete_file(file1)
        delete_file(file2)


# URLs to raw CSV files on GitHub
f1_url = ('https://raw.githubusercontent.com/dntpanix/automation_qa/main'
          '/ideas_for_test/work_with_csv/random.csv')
f2_url = ('https://raw.githubusercontent.com/dntpanix/automation_qa/main'
          '/ideas_for_test/work_with_csv/random-michaels.csv')
csv3 = 'result_Putintsev.csv'

print(csv_duplicate_remover(f1_url, f2_url, csv3))
