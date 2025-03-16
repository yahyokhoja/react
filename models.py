from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Модель пользователя
class User(AsyncAttrs, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Связь один-ко-многим: у пользователя могут быть заказы
    orders = relationship("Order", back_populates="user")

# Модель товара
class Product(AsyncAttrs, Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)

# Модель заказа
class Order(AsyncAttrs, Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    # Связи между таблицами
    user = relationship("User", back_populates="orders")
    product = relationship("Product")