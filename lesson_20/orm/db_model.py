"""Db orm models."""

from sqlalchemy import Column, ForeignKey, Integer, String

from db_orm import Base


class Categories(Base):
    """Table categories."""

    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class Products(Base):
    """Table products."""

    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(50))
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
