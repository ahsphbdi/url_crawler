"""New Migration

Revision ID: bc7914a7316d
Revises: 734986920845
Create Date: 2024-01-24 23:44:17.199540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc7914a7316d'
down_revision = '734986920845'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'uuid',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.String(length=63),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'uuid',
               existing_type=sa.String(length=63),
               type_=sa.VARCHAR(length=32),
               existing_nullable=False)
    # ### end Alembic commands ###