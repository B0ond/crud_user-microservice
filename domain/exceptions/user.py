from uuid import UUID

from pydantic import EmailStr

class UserEmailNotFound(Exception):
    """Пользователь по Email не найден"""
    def __init__(self, email: EmailStr) -> None:
        self.email = email

    def __str__(self) -> str:
        return f"Пользователь с email {self.email} не найден"

class UserIdNotFound(Exception):
    """Пользователь по Id не найден"""
    def __init__(self, user_id: UUID) -> None:
        self.user_id = user_id
    def __str__(self) -> str:
        return f"Пользователь с id {self.user_id} не найден"

class UserAlreadyExists(Exception):
    """Пользователь уже существует"""
    def __init__(self, email: EmailStr) -> None:
        self.email = email

    def __str__(self) -> str| None:
        if self.email:
            return f'Пользователь с email {self.email} уже существует'
