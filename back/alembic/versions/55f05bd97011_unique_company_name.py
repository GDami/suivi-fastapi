"""unique company name

Revision ID: 55f05bd97011
Revises: 3b4cf204c0a6
Create Date: 2026-02-23 12:24:51.479893

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55f05bd97011'
down_revision: Union[str, Sequence[str], None] = '3b4cf204c0a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint('uq_company_name', 'company', ['name'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('uq_company_name', 'company', type_='unique')
