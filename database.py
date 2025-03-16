from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL для подключения к SQLite (асинхронный режим)
DATABASE_URL = "sqlite+aiosqlite:///./shop.db"

# Создаем движок базы данных
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаем базовый класс для моделей
Base = declarative_base()

# Фабрика сессий
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Функция для получения сессии
async def get_db():
    async with SessionLocal() as session:
        yield session