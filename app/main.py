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