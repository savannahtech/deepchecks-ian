"""modify id field to primary key

Revision ID: 26f7ab1f7c1a
Revises: 85bbf0b1a627
Create Date: 2024-07-04 16:07:47.190300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26f7ab1f7c1a'
down_revision: Union[str, None] = '85bbf0b1a627'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE SEQUENCE IF NOT EXISTS metrics_id_seq;
        ALTER TABLE metrics
        ALTER COLUMN id SET DEFAULT nextval('metrics_id_seq'),
        ALTER COLUMN id SET NOT NULL,
        ADD PRIMARY KEY (id);""")


def downgrade() -> None:
    pass
