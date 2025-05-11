from abc import ABC, abstractmethod
from uuid import UUID
from application.services.user import UserCreateSchema, UserReadSchema



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
    async def get_by_email(self, email: str) -> UserReadSchema | None:
        """Получить пользователя по email"""
        pass

