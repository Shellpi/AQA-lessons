"""Homework 20."""
import csv

import db_model
from db_orm import Db
from sqlalchemy.exc import SQLAlchemyError

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


def populate_db_from_csv(db, categories_file, products_file):
    """Populate the database with data from CSV files."""
    try:
        with open(categories_file, 'r') as cat_file:
            reader = csv.DictReader(cat_file)
            categories = [db_model.Categories(name=row['name'])
                          for row in reader]
            db.session.add_all(categories)

        with open(products_file, 'r') as prod_file:
            reader = csv.DictReader(prod_file)
            products = [
                db_model.Products(
                    name=row['name'],
                    description=row['description'],
                    price=row['price'],
                    category_id=row['category_id'],
                )
                for row in reader
            ]
            db.session.add_all(products)

        db.session.commit()
        print('Database populated successfully from CSV files!')
    except SQLAlchemyError as err:
        db.session.rollback()
        print(f'Error populating database: {err}')
    except FileNotFoundError as err:
        print(f'CSV file not found: {err}')
    except KeyError as err:
        print(f'Missing column in CSV file: {err}')


def fetch_products(db):
    """Fetch and display products with their categories."""
    try:
        result = (
            db.session.query(
                db_model.Categories.name.label('category_name'),
                db_model.Products.name.label('product_name'),
                db_model.Products.description.label('product_description'),
                db_model.Products.price.label('product_price'),
            )
            .join(db_model.Products, db_model.Categories.id == db_model.Products.category_id)
            .order_by(db_model.Categories.name)
            .all()
        )

        for row in result:
            print(f'Category: {row.category_name}, '
                  f'Product: {row.product_name}, '
                  f'Description: {row.product_description}, '
                  f'Price: {row.product_price}')

    except SQLAlchemyError as err:
        print(f'Error fetching products: {err}')


if __name__ == '__main__':
    db = Db()
    categories_csv = 'categories.csv'
    products_csv = 'products.csv'
    populate_db_from_csv(db, categories_csv, products_csv)
    fetch_products(db)
