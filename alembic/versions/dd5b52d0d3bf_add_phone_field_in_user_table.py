"""add phone field in user table

Revision ID: dd5b52d0d3bf
Revises: e7efe927c52b
Create Date: 2025-05-06 14:43:17.582814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd5b52d0d3bf'
down_revision: Union[str, None] = 'e7efe927c52b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone', sa.String(length=10), nullable=False))
    op.create_unique_constraint('uq_user_phone', 'user', ['phone'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_user_phone', 'user', type_='unique')
    op.drop_column('user', 'phone')
    # ### end Alembic commands ###
