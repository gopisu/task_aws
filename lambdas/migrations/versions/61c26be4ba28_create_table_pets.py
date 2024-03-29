"""Create table Pets

Revision ID: 61c26be4ba28
Revises: adfdbb1f8172
Create Date: 2024-02-21 22:50:23.314636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61c26be4ba28'
down_revision = 'adfdbb1f8172'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.String(length=200), nullable=False),
    sa.Column('type', sa.String(length=200), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    # ### end Alembic commands ###
