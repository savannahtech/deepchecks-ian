"""create metrics table

Revision ID: 283e610fc97c
Revises: 9ba0bd62b3fa
Create Date: 2024-07-04 12:48:58.383061

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '283e610fc97c'
down_revision: Union[str, None] = '9ba0bd62b3fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'metrics',
        sa.Column('id', sa.Integer, index=True, autoincrement=True, nullable=False),
        sa.Column('log_id', sa.Integer, nullable=False),
        sa.Column('input_metric_alert', sa.Text(), nullable=False),
        sa.Column('output_metric_alert', sa.Text(), nullable=True),
    )


def downgrade() -> None:
    pass
