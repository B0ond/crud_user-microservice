from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.db.models.base import BaseOrm


class User(BaseOrm):
    """ORM модель пользователя (таблица users)"""
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column( primary_key=True)
    user_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]

