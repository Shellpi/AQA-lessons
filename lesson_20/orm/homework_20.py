"""Homework 20."""

import db_model
from db_orm import Db

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

db = Db()

categories = [
    db_model.Categories(name='vegetables'),
    db_model.Categories(name='soda'),
    db_model.Categories(name='fruits'),
    db_model.Categories(name='candies'),
]


products = [
    db_model.Products(name='cola',
                      description='coca-cola 2l', price=25, category_id=2),
    db_model.Products(name='potato',
                      description='potato delicious',
                      price=10, category_id=1),
    db_model.Products(name='golden apples',
                      description='tasty golden apples',
                      price=20, category_id=3),
    db_model.Products(name='fanta',
                      description='orange soda 2l',
                      price=25, category_id=2),
    db_model.Products(name='cucumber',
                      description='fresh cucumber',
                      price=19, category_id=1),
    db_model.Products(name='onion',
                      description='sweet onion',
                      price=29, category_id=1),
    db_model.Products(name='Sprite',
                      description='Sprite 1.5l',
                      price=20, category_id=2),
]

db.session.add_all(categories)
db.session.add_all(products)
db.session.commit()

result = (db.session.query(
    db_model.Categories.name.label('category_name'),
    db_model.Products.name.label('product_name'),
    db_model.Products.description.label('product_description'),
    db_model.Products.price.label('product_price'))
    .join(db_model.Products, db_model.Categories.id == db_model.Products.category_id)
    .order_by(db_model.Categories.name).all())

for row in result:
    print(f'Category: {row.category_name}, '
          f'Product: {row.product_name}, '
          f'Description: {row.product_description}, '
          f'Price: {row.product_price}')
