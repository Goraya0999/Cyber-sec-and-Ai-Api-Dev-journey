from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from App.db.session import Base
from App.models.associations import user_roles

if TYPE_CHECKING:
    from App.models.user import User


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)

    users: Mapped[list["User"]] = relationship(
        secondary=user_roles, back_populates="roles"
    )

    def __repr__(self) -> str:  # pragma: no cover
        return f"<Role {self.name}>"


# Canonical role names seeded by the Alembic data migration
ADMIN = "admin"
MODERATOR = "moderator"
USER = "user"
ALL_ROLES = (ADMIN, MODERATOR, USER)
