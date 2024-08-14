"""create reserves table

Revision ID: dea7f0ef9276
Revises: 
Create Date: 2024-08-07 09:38:28.768418

"""
from typing import Sequence, Union
import datetime

from sqlalchemy.sql import func
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision: str = 'dea7f0ef9276'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        'line_reserves',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('reservation_id', sa.Integer, nullable=False),
        sa.Column('reservation_date', sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column('check_in', sa.Date, nullable=False),
        sa.Column('check_out', sa.Date, nullable=False),
        sa.Column('line_id', sa.String(255), nullable=False),
        sa.Column('status', sa.String(20), nullable=False),
        sa.Column('count_of_person', sa.Integer, nullable=False),
        sa.Column('room_type', sa.String(20), nullable=False),
        sa.Column('option_id', sa.Integer, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    )

def downgrade():
    op.drop_table('line_reserves')
