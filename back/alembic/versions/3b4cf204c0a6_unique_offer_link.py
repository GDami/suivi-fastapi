"""unique offer link

Revision ID: 3b4cf204c0a6
Revises: c3baa48ec4fd
Create Date: 2026-02-23 12:18:44.538250

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b4cf204c0a6'
down_revision: Union[str, Sequence[str], None] = 'c3baa48ec4fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint('uq_offer_link', 'offer', ['link'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('uq_offer_link', 'offer', type_='unique')
