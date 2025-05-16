"""Create jobs table

Revision ID: 657ed922e51b
Revises: 
Create Date: 2025-05-15 23:26:02.082193

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM


# revision identifiers, used by Alembic.
revision: str = '657ed922e51b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create the jobstatus enum
    jobstatus_enum = ENUM(
        "PENDING",
        "PROCESSING",
        "SUCCESS",
        "FAILED",
        name="jobstatus",
        create_type=True,
    )
    # op.execute(
    #     "CREATE TYPE jobstatus AS ENUM ('PENDING', 'PROCESSING', 'SUCCESS', 'FAILURE')"
    # )

    op.create_table(
        "jobs",
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("repo_url", sa.String, nullable=False),
        sa.Column("language", sa.String, nullable=False),
        sa.Column("generate_docs", sa.Boolean, default=False),
        sa.Column("generate_tests", sa.Boolean, default=False),
        sa.Column("status", jobstatus_enum, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table("jobs")
    op.execute("DROP TYPE jobstatus")  # Drop the ENUM type
