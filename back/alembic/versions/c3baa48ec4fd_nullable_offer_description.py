"""nullable offer description

Revision ID: c3baa48ec4fd
Revises: 
Create Date: 2026-02-23 09:17:17.553269

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3baa48ec4fd'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('offer', 'description', existing_type=sa.VARCHAR(), nullable=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('offer', 'description', existing_type=sa.VARCHAR(), nullable=False)
