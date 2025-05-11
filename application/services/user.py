from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime


class ReadModel(BaseModel):
    """для удобства чтения объектов модели данных в виде словарей"""
    class Config:
        orm_mode = True  # по умолчанию pydantic работает только с dict,
        # поэтому нужно сказать ему что работаем с ORM объектами


class UserCreateSchema(BaseModel):
    """Создание пользователя (входные данные от клиента)"""
    email: EmailStr  # проверяет, что это валидная почта
    name: str = Field(..., min_length=1, max_length=300, title="Имя пользователя")


class UserReadSchema(ReadModel):
    """Ответ клиенту (чтение пользователя)"""
    id: UUID
    email: EmailStr
    name: str
    created_at: datetime


class UserUpdateSchema(BaseModel):
    """Обновление пользователя"""
    email: EmailStr | None = None
    name: str | None = None
