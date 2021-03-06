"""empty message

Revision ID: 3d0c43f03396
Revises: 
Create Date: 2020-11-25 16:20:31.547976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d0c43f03396'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=500), nullable=False),
    sa.Column('contact_info', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_customers_full_name'), 'customers', ['full_name'], unique=False)
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ordered_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('suppliers', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_products_description'), 'products', ['description'], unique=False)
    op.create_index(op.f('ix_products_name'), 'products', ['name'], unique=False)
    op.create_table('shipments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tracking_no', sa.String(length=500), nullable=True),
    sa.Column('products', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_shipments_tracking_no'), 'shipments', ['tracking_no'], unique=False)
    op.create_table('suppliers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('contact_info', sa.JSON(), nullable=False),
    sa.Column('products', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_suppliers_name'), 'suppliers', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_suppliers_name'), table_name='suppliers')
    op.drop_table('suppliers')
    op.drop_index(op.f('ix_shipments_tracking_no'), table_name='shipments')
    op.drop_table('shipments')
    op.drop_index(op.f('ix_products_name'), table_name='products')
    op.drop_index(op.f('ix_products_description'), table_name='products')
    op.drop_table('products')
    op.drop_table('orders')
    op.drop_index(op.f('ix_customers_full_name'), table_name='customers')
    op.drop_table('customers')
    # ### end Alembic commands ###
