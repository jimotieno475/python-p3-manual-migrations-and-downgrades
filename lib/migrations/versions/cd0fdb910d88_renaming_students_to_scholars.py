"""Renaming students to scholars

Revision ID: cd0fdb910d88
Revises: 791279dd0760
Create Date: 2023-12-06 14:30:56.292481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd0fdb910d88'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
