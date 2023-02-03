"""Add sweepcast table

Revision ID: 3912a5f2c4e8
Revises: 
Create Date: 2022-10-20 16:23:07.659840

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "3912a5f2c4e8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "sweepcast",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("date_timestamp", sa.DateTime(), nullable=True),
        sa.Column("ticker", sa.String(length=10), nullable=True),
        sa.Column("activity_type", sa.String(length=200), nullable=True),
        sa.Column("put_or_call", sa.String(length=10), nullable=True),
        sa.Column("sentiment", sa.String(length=10), nullable=True),
        sa.Column("sweep_score", sa.Float(), nullable=True),
        sa.Column("vol_oi_ratio", sa.String(length=200), nullable=True),
        sa.Column("strike_price", sa.Float(), nullable=True),
        sa.Column("expiration", sa.Date(), nullable=True),
        sa.Column("premium", sa.Integer(), nullable=True),
        sa.Column("details", sa.String(length=200), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("sweepcast")
    # ### end Alembic commands ###
