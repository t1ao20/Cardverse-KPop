"""Add column cn to users

Revision ID: 601c51ce752d
Revises: 
Create Date: 2024-12-12 22:41:22.917633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '601c51ce752d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cn', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('cn')

    # ### end Alembic commands ###
