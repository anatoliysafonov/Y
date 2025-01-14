"""first

Revision ID: 027b51c21cb7
Revises: bde886b346e8
Create Date: 2023-09-10 20:36:14.559356

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '027b51c21cb7'
down_revision: Union[str, None] = 'bde886b346e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_index('ix_photo_description', table_name='photo')
    op.drop_index('ix_photo_name', table_name='photo')
    op.drop_index('ix_photo_photo_url', table_name='photo')
    op.drop_table('photo')
    op.drop_table('ratings')
    op.drop_table('tags')
    op.drop_table('users')
    op.drop_table('photo_m2m_tag')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photo_m2m_tag',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('photo_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tag_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photo.id'], name='photo_m2m_tag_photo_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], name='photo_m2m_tag_tag_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='photo_m2m_tag_pkey')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=250), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('avatar', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('refresh_token', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('banned', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('confirmed', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('role', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('uploaded_photos', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('tags',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='tags_pkey'),
    sa.UniqueConstraint('name', name='tags_name_key')
    )
    op.create_table('ratings',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('rating', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('photo_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photo.id'], name='ratings_photo_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='ratings_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='ratings_pkey')
    )
    op.create_table('photo',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('photo_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=300), autoincrement=False, nullable=False),
    sa.Column('photo_url', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rating', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='photo_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='photo_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_photo_photo_url', 'photo', ['photo_url'], unique=False)
    op.create_index('ix_photo_name', 'photo', ['name'], unique=False)
    op.create_index('ix_photo_description', 'photo', ['description'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('content', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('photo_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photo.id'], name='comments_photo_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='comments_user_id_fkey', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='comments_pkey')
    )
    # ### end Alembic commands ###
