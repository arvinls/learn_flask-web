"""add some column

Revision ID: 23dd43edf649
Revises: 5a01bc2316e0
Create Date: 2015-03-29 18:58:16.100000

"""

# revision identifiers, used by Alembic.
revision = '23dd43edf649'
down_revision = '5a01bc2316e0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###