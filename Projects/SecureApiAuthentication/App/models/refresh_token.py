from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from App.db.session import Base

if TYPE_CHECKING:
    from App.models.user import User


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )

    # SHA-256 hash of the raw token. The raw value is only ever sent to the
    # client — a DB leak alone can never be replayed as a session takeover.
    token_hash: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)

    # Groups a token and everything it was rotated into. If a revoked token in
    # this family is ever reused, the whole family is revoked (replay defense).
    family_id: Mapped[UUID] = mapped_column(nullable=False, default=uuid4, index=True)

    device_info: Mapped[str | None] = mapped_column(String(255), nullable=True)

    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    revoked: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    user: Mapped["User"] = relationship(back_populates="refresh_tokens")
