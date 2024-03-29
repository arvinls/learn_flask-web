"""empty message

Revision ID: 198c858cf7b2
Revises: 41bd8aaae7a0
Create Date: 2015-04-02 07:26:56.641000

"""

# revision identifiers, used by Alembic.
revision = '198c858cf7b2'
down_revision = '41bd8aaae7a0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(u'ix_posts_timestamp', 'posts', ['timestamp'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(u'ix_posts_timestamp', table_name='posts')
    op.drop_table('posts')
    ### end Alembic commands ###
