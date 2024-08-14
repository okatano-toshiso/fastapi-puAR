"""create line_users table

Revision ID: ed6b534948f5
Revises: dea7f0ef9276
Create Date: 2024-08-07 17:06:28.516379

"""

from typing import Sequence, Union
import datetime

from sqlalchemy.sql import func
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'ed6b534948f5'
down_revision: Union[str, None] = 'dea7f0ef9276'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        'line_users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('line_id', sa.String(255), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('name_kana', sa.String(255), nullable=True),
        sa.Column('phone_number', sa.String(255), nullable=False),
        sa.Column('age', sa.Integer, nullable=True),
        sa.Column('adult', sa.Boolean, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    )

def downgrade():
    op.drop_table('line_users')
