"""message

Revision ID: eb229b3491ed
Revises: 
Create Date: 2023-07-06 22:45:16.640558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb229b3491ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address_1', sa.String(), nullable=False),
    sa.Column('address_2', sa.String(), nullable=False),
    sa.Column('address_city', sa.String(), nullable=False),
    sa.Column('address_state', sa.String(), nullable=False),
    sa.Column('address_postal', sa.Integer(), nullable=False),
    sa.Column('addess_type_of', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_addresses'))
    )
    op.create_table('cart_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_quantity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cart_items'))
    )
    op.create_table('cartstuff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cartstuff'))
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('categories', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_categories'))
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_comment', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_comments'))
    )
    op.create_table('order_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('num_of_items', sa.Integer(), nullable=True),
    sa.Column('items_price', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order_items'))
    )
    op.create_table('order_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('current_status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order_status'))
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_total', sa.Integer(), nullable=True),
    sa.Column('order_status', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_orders'))
    )
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('card_number', sa.Integer(), nullable=True),
    sa.Column('cardholder_name', sa.String(), nullable=True),
    sa.Column('expiration_month', sa.Integer(), nullable=True),
    sa.Column('expiration_year', sa.Integer(), nullable=True),
    sa.Column('cvv', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_payments'))
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('p_name', sa.String(), nullable=False),
    sa.Column('p_description', sa.String(), nullable=False),
    sa.Column('p_price', sa.Integer(), nullable=False),
    sa.Column('p_image', sa.String(), nullable=False),
    sa.Column('p_image_2', sa.String(), nullable=True),
    sa.Column('p_background', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_products'))
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_rating', sa.String(), nullable=False),
    sa.Column('review_text', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_reviews'))
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roles', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_roles'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('reviews')
    op.drop_table('products')
    op.drop_table('payments')
    op.drop_table('orders')
    op.drop_table('order_status')
    op.drop_table('order_items')
    op.drop_table('comments')
    op.drop_table('categories')
    op.drop_table('cartstuff')
    op.drop_table('cart_items')
    op.drop_table('addresses')
    # ### end Alembic commands ###