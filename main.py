from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(root_path="/api")

# Модели данных
class Product(BaseModel):
    name: str
    description: str
    price: float

# Список продуктов (имитируем базу данных)
products = [
    {"name": "Laptop", "description": "A powerful laptop", "price": 1200.99},
    {"name": "Phone", "description": "A smartphone", "price": 799.99}
]
@app.get("/")
def root():
    return {"message": "Добро пожаловать в API магазина!"}


# Маршрут для получения всех продуктов
@app.get("/products", response_model=List[Product])
def get_products():
    return products

# Маршрут для получения одного продукта по имени
@app.get("/products/{product_name}", response_model=Product)
def get_product(product_name: str):
    for product in products:
        if product["name"].lower() == product_name.lower():
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Маршрут для добавления нового продукта
@app.post("/products", response_model=Product)
def add_product(product: Product):
    products.append(product.dict())
    return product

# Маршрут для удаления продукта по имени
@app.delete("/products/{product_name}", response_model=Product)
def delete_product(product_name: str):
    for product in products:
        if product["name"].lower() == product_name.lower():
            products.remove(product)
            return product
    raise HTTPException(status_code=404, detail="Product not found")