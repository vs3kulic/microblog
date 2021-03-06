"""extended user model with new fields

Revision ID: 92f772745dcd
Revises: 3d28ca2427c3
Create Date: 2021-08-09 14:26:48.715146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92f772745dcd'
down_revision = '3d28ca2427c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
