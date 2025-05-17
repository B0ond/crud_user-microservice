from typing import Any, Coroutine
from uuid import UUID
from pydantic import EmailStr
from domain.schemas.user import UserCreateSchema, UserReadSchema, UserUpdateSchema
from domain.exceptions.user import UserEmailNotFound, UserIdNotFound, UserAlreadyExists
from domain.repositories.user import AbstractUserRepository

class UsersService:
    """Сервис для работы с пользователями.

    Методы:
        - create_user - создание нового пользователя
        - get_user_by_email - получение пользователя по email
        - get_user_by_id - получение пользователя по id
        - update_user - обновление пользователя
        - get_all_users - получение всех пользователей
        - delete_user - удаление пользователя

    """
    def __init__(self, user_repo: AbstractUserRepository) -> None:
        self.user_repo = user_repo

    async def create_user(self, user_data: UserCreateSchema) -> UserReadSchema:
        """Создание пользователя"""
        existing_user = await self.user_repo.get_by_email(user_data.email)
        if existing_user:
            raise UserAlreadyExists(email=user_data.email)
        new_user = await self.user_repo.create_user(user_data) # create_user_repo принимает UserCreateSchema
        return new_user


    async def get_user_by_email(self, email: EmailStr) -> UserReadSchema:
        """Получение пользователя по email"""
        #  т.к email уникален
        existing_user = await self.user_repo.get_by_email(email)
        if not existing_user:
            raise UserEmailNotFound(email=email)
        return existing_user


    async def get_user_by_id(self, user_id: UUID) -> UserReadSchema:
        """Получение пользователя по id"""
        existing_user = await self.user_repo.get_by_id(user_id)
        if not existing_user:
            raise UserIdNotFound(user_id=user_id)
        return existing_user


    async def update_user(self,
                          user_id: UUID,
                          user_data: UserUpdateSchema
                          ) -> UserReadSchema | None:
        """Обновление пользователя"""
        existing_user = await self.user_repo.get_by_id(user_id)
        if not existing_user:
            raise UserIdNotFound(user_id=user_id)
        if not user_data:
            raise ValueError("Данные для обновления не предоставлены")
        updated_user = await self.user_repo.update_user(user_id, user_data)
        if not updated_user:
            return updated_user

    async def get_all_users(self) -> list[UserReadSchema]:
        """Получение всех пользователей"""
        return await self.user_repo.get_all()

    async def delete_user(self, user_id: UUID) -> None:
        """Удаление пользователя"""
        existing_user = await self.user_repo.get_by_id(user_id)
        if not existing_user:
            raise UserIdNotFound(user_id=user_id)
        return await self.user_repo.delete_user(user_id)
