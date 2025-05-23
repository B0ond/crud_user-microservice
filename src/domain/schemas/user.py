from pydantic import BaseModel, EmailStr, Field, ConfigDict
from uuid import UUID, uuid4
from datetime import datetime


class ReadModel(BaseModel):
    """для удобства чтения объектов модели данных в виде словарей"""
    model_config = ConfigDict(from_attributes=True)  # по умолчанию pydantic работает только с dict,
        # поэтому нужно сказать ему что работаем с ORM объектами


class UserCreateSchema(BaseModel):
    """Создание пользователя (входные данные от клиента)"""
    id: UUID = Field(default_factory=uuid4, alias="_id")
    email: EmailStr = Field(...)
    email: EmailStr  # проверяет, что это валидная почта
    name: str = Field(..., min_length=1, max_length=50, title="Имя пользователя")


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
