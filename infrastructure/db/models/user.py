from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Column
from sqlalchemy.orm import DeclarativeBase
from uuid import UUID, uuid4
from datetime import datetime, timezone

class User(DeclarativeBase):
    __tablename__ = 'user'
