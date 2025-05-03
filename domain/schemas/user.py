from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime


class UserCreate(BaseModel):
    """Схема для создания пользователя (входные данные от клиента)"""
    email: EmailStr  # проверяет, что это валидная почта
    name: str = Field(..., min_length=1, max_length=100)  # имя пользователя


class UserUpdate(BaseModel):
    """Схема для обновления пользователя"""
    email: EmailStr | None = None  # можно не обновлять
    name: str | None = None


class UserRead(BaseModel):
    """Схема для ответа клиенту (чтение пользователя)"""
    id: UUID
    email: EmailStr
    name: str
    created_at: datetime

    class Config:
        orm_mode = True  # позволяет использовать SQLAlchemy объекты
