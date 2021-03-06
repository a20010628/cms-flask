"""empty message

Revision ID: 1cd45ec3b520
Revises: dbc571c79e61
Create Date: 2022-06-18 20:56:32.911538

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1cd45ec3b520'
down_revision = 'dbc571c79e61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('front_user',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('telephone', sa.String(length=11), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('_password', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('realname', sa.String(length=50), nullable=True),
    sa.Column('avatar', sa.String(length=100), nullable=True),
    sa.Column('signature', sa.String(length=100), nullable=True),
    sa.Column('gender', sa.Enum('MALE', 'FEMALE', 'SECRET', 'UNKNOW', name='genderenum'), nullable=True),
    sa.Column('join_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('telephone')
    )
    op.alter_column('cms_user', 'email',
               existing_type=mysql.VARCHAR(charset='utf8', length=50),
               type_=sa.String(length=500),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cms_user', 'email',
               existing_type=sa.String(length=500),
               type_=mysql.VARCHAR(charset='utf8', length=50),
               existing_nullable=False)
    op.drop_table('front_user')
    # ### end Alembic commands ###
