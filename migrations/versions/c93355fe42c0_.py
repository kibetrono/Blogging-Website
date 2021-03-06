"""empty message

Revision ID: c93355fe42c0
Revises: d1ce9240b11d
Create Date: 2022-02-13 12:26:22.343344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c93355fe42c0'
down_revision = 'd1ce9240b11d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscribes_email'), 'subscribes', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subscribes_email'), table_name='subscribes')
    op.drop_table('subscribes')
    # ### end Alembic commands ###
