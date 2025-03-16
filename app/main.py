from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, products, orders

# Создаём таблицы в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Shop", description="Интернет-магазин на FastAPI", version="1.0")

# Подключаем маршруты
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

@app.get("/")
def root():
    return {"message": "Добро пожаловать в FastAPI Shop!"}


from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Пример списка товаров
products = [
    {"id": 1, "name": "Товар 1", "price": 100},
    {"id": 2, "name": "Товар 2", "price": 200},
    {"id": 3, "name": "Товар 3", "price": 300},
]

cart_items = []

# Получить список товаров
@app.get("/api/products", response_model=List[dict])
async def get_products():
    return products

# Добавить товар в корзину
@app.post("/api/cart")
async def add_to_cart(product: dict):
    cart_items.append(product)
    return {"message": "Товар добавлен в корзину!"}

# Получить товары в корзине
@app.get("/api/cart", response_model=List[dict])
async def get_cart():
    return cart_items
