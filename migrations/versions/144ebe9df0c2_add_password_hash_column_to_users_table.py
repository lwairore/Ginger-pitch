"""Add password_hash column to users table.

Revision ID: 144ebe9df0c2
Revises: 6f8e388cabe8
Create Date: 2019-05-26 06:40:13.150913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '144ebe9df0c2'
down_revision = '6f8e388cabe8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###