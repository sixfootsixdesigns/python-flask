"""empty message

Revision ID: 293c85c45153
Revises: 
Create Date: 2020-06-01 22:36:35.298825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '293c85c45153'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(length=64), nullable=True),
    sa.Column('term_start', sa.String(length=120), nullable=True),
    sa.Column('term_end', sa.String(length=120), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_application_state'), 'application', ['state'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_application_state'), table_name='application')
    op.drop_table('application')
    # ### end Alembic commands ###
