"""Initial migration.

Revision ID: 855fbfe44cde
Revises: 
Create Date: 2024-10-15 13:56:39.386913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '855fbfe44cde'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
