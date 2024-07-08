"""edit metrics table

Revision ID: b73c28d288a9
Revises: 283e610fc97c
Create Date: 2024-07-04 13:53:38.374466

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b73c28d288a9'
down_revision: Union[str, None] = '283e610fc97c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('metrics', sa.Column('metric', sa.Integer, nullable=True))

def downgrade() -> None:
    pass
