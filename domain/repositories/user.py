from abc import ABC, abstractmethod
from uuid import UUID
from pydantic import EmailStr
from domain.schemas.user import UserCreateSchema, UserReadSchema, UserUpdateSchema


class AbstractUserRepository(ABC):
    """Абстрактный класс репозитория пользователей"""

    @abstractmethod
    async def create_user(self, user: UserCreateSchema) -> UserReadSchema:
        """Создать пользователя"""
        pass

    @abstractmethod
    async def get_by_id(self, user_id: UUID) -> UserReadSchema | None:
        """Получить пользователя по id"""
        pass

    @abstractmethod
    async def get_by_email(self, email: EmailStr) -> UserReadSchema | None:
        """Получить пользователя по email"""
        pass

    @abstractmethod
    async def update_user(self, user: UserUpdateSchema) -> UserReadSchema:
        """Обновить пользователя"""
        pass
        # TODO: добавить обновление почты т.к. она уникальная

    @abstractmethod
    async def delete_user(self, user_id: UUID) -> None:
        """Удалить пользователя"""
        pass
