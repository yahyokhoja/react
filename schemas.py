from pydantic import BaseModel, EmailStr
from typing import Optional

# Схема для пользователя (без пароля)
class UserBase(BaseModel):
    username: str
    email: EmailStr

# Схема для создания пользователя (включает пароль)
class UserCreate(UserBase):
    password: str

# Схема для отображения пользователя (без пароля)
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

# Схема товара
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# Схема для создания товара
class ProductCreate(ProductBase):
    pass

# Схема для отображения товара
class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True

# Схема заказа
class OrderBase(BaseModel):
    user_id: int
    product_id: int

# Схема для создания заказа
class OrderCreate(OrderBase):
    pass

# Схема для отображения заказа
class OrderResponse(OrderBase):
    id: int

    class Config:
        from_attributes = True