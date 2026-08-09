"""seed default roles

Revision ID: c1a2b3d4e5f6
Revises: b847b35b6c47
Create Date: 2026-08-09 09:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "c1a2b3d4e5f6"
down_revision: Union[str, Sequence[str], None] = "b847b35b6c47"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

roles_table = sa.table("roles", sa.column("id", sa.Integer), sa.column("name", sa.String))

DEFAULT_ROLES = ["admin", "moderator", "user"]


def upgrade() -> None:
    op.bulk_insert(roles_table, [{"name": name} for name in DEFAULT_ROLES])


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(roles_table.delete().where(roles_table.c.name.in_(DEFAULT_ROLES)))
