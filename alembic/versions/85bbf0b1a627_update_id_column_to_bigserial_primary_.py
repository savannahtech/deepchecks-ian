"""Update id column to BIGSERIAL PRIMARY KEY

Revision ID: 85bbf0b1a627
Revises: b73c28d288a9
Create Date: 2024-07-04 14:39:38.697696

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85bbf0b1a627'
down_revision: Union[str, None] = 'b73c28d288a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('metrics', 'id',
                    existing_type=sa.Integer(),
                    type_=sa.BigInteger(),
                    existing_nullable=False,
                    autoincrement=True)


def downgrade() -> None:
    op.alter_column('metrics', 'id',
                    existing_type=sa.BigInteger(),
                    type_=sa.Integer(),
                    existing_nullable=False,
                    autoincrement=True)
