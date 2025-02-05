"""Homework 20."""
import csv
import logging
import sqlite3

"""
Створіть базу даних для інтернет-магазину з наступними таблицями:
products: таблиця для зберігання інформації про продукти,
включаючи назву, опис, ціну тощо.
categories: таблиця для категорій продуктів.
products повинна мати зовнішній ключ на таблицю categories.
Напишіть SQL-скрипт для створення зазначених таблиць.
Внесіть декілька рядків даних в кожну таблицю
Виконайте JOIN-запит, який повертає інформацію про продукти
та назву їх категорій
"""

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def create_tables():
    """Create tables."""
    with sqlite3.connect('internet_shop.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL CHECK (price >= 0),
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories (id)
            )
        """)
        logging.info('Tables created successfully.')


def populate_tables_from_csv(categories_csv, products_csv):
    """Populate the table from CSV files."""
    with sqlite3.connect('internet_shop.db') as conn:
        cursor = conn.cursor()
        try:
            # Populate categories
            with open(categories_csv, 'r') as cat_file:
                reader = csv.DictReader(cat_file)
                categories = [(row['name'],) for row in reader]
                if categories:
                    cursor.executemany('INSERT INTO categories'
                                       ' (name) VALUES (?)', categories)
                    logging.info('Categories data inserted successfully.')
                else:
                    logging.warning('Categories CSV is empty.')

            # Populate products
            with open(products_csv, 'r') as prod_file:
                reader = csv.DictReader(prod_file)
                products = [
                    (row['name'],
                     row['description'],
                     int(row['price']),
                     int(row['category_id']))
                    for row in reader
                ]
                if products:
                    cursor.executemany(
                        'INSERT INTO products (name, description, '
                        'price, category_id) VALUES (?, ?, ?, ?)',
                        products,
                    )
                    logging.info('Products data inserted successfully.')
                else:
                    logging.warning('Products CSV is empty.')

            conn.commit()
        except FileNotFoundError as err:
            logging.error(f'CSV file not found: {err}')
        except KeyError as err:
            logging.error(f'Missing column in CSV file: {err}')
        except Exception as err:
            logging.error(f'Unexpected error: {err}')


def join_tables_with_category_id():
    """Perform JOIN and print results."""
    with sqlite3.connect('internet_shop.db') as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT categories.name AS category_name,
               products.name AS product_name,
               products.description AS product_description,
               products.price AS product_price
        FROM categories
        JOIN products ON categories.id = products.category_id
        ORDER BY categories.name, products.name
        """)

        rows = cursor.fetchall()
        logging.info('Join query executed successfully. Results:')
        for row in rows:
            print(row)


if __name__ == '__main__':
    try:
        create_tables()
        categories_csv = 'categories.csv'
        products_csv = 'products.csv'
        populate_tables_from_csv(categories_csv, products_csv)
        join_tables_with_category_id()
    except Exception as err:
        logging.error(f'Unexpected error: {err}')
