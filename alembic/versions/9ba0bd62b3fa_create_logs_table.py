"""create logs table

Revision ID: 9ba0bd62b3fa
Revises: 
Create Date: 2024-07-03 22:20:32.290647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9ba0bd62b3fa'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'logs',
        sa.Column('id', sa.Integer, index=True),
        sa.Column('input', sa.Text(), nullable=False),
        sa.Column('output', sa.Text(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('account')
