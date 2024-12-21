"""Homework 20."""

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

with sqlite3.connect('internet_shop.db') as conn:
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
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

    categories = [
        ('vegetables', 'vegetable category'),
        ('soda', 'soda category'),
        ('fruits', 'fruits category'),
        ('candies', 'candies category'),
    ]
    cursor.executemany('INSERT INTO categories (name, '
                       'description) VALUES (?, ?)', categories)

    products = [
        ('cola', 'coca-cola 2l', 25, 2),
        ('potatoe', 'potatoe delicious', 10, 1),
        ('golden apples', 'tasty golden apples', 20, 3),
        ('fanta', 'orange soda 2l', 25, 2),
        ('cucumber', 'best cucumber', 19, 1),
        ('onion', 'sweet onion', 29, 1),
        ('Sprite', 'Sprite 1.5l', 20, 2),
    ]
    cursor.executemany('INSERT INTO products (name, description, '
                       'price, category_id) VALUES (?, ?, ?, ?)', products)

    conn.commit()

    cursor.execute("""
    SELECT categories.name AS category_name,
           categories.description AS category_description,
           products.name AS product_name,
           products.description AS product_description,
           products.price AS product_price
    FROM categories
    JOIN products ON categories.id = products.category_id
    ORDER BY categories.name, products.name
    """)

    rows = cursor.fetchall()
    print('Join Results:')
    for row in rows:
        print(row)
