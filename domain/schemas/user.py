from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime


class BaseSchema(BaseModel):
    """для удобства чтения объектов модели данных в виде словарей"""
    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    """Создание пользователя (входные данные от клиента)"""
    email: EmailStr  # проверяет, что это валидная почта
    name: str = Field(..., min_length=1, max_length=300, title="Имя пользователя")


class UserUpdateSchema(BaseModel):
    """Обновление пользователя"""
    email: EmailStr | None = None
    name: str | None = None


class UserReadSchema(BaseSchema):
    """Ответ клиенту (чтение пользователя)"""
    id: UUID
    email: EmailStr
    name: str
    created_at: datetime
