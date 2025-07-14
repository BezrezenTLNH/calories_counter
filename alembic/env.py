import os
import sys
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context  # type: ignore
from app.core.config import settings  # Load DATABASE_URL from .env
from app.db.models import Base  # Import all models for autogenerate support

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Alembic config object, provides access to values within the .ini file
config = context.config

# Set up logging using the config file
fileConfig(config.config_file_name)

# Override sqlalchemy.url in alembic.ini with the value from settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Set target_metadata for 'autogenerate' support (model diffing)
target_metadata = Base.metadata


# Create an async SQLAlchemy engine using Alembic config
def get_engine():
    return async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        future=True,
    )


# Run migrations in "online" mode using async engine
async def run_migrations_online():
    connectable = get_engine()
    async with connectable.connect() as connection:
        await connection.run_sync
        (do_run_migrations)  # Run migrations in sync context


# Migration logic: configure Alembic context and run migrations
def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,  # Detect column type changes
    )
    with context.begin_transaction():
        context.run_migrations()


# Entry point: only online mode is supported for async migrations
if context.is_offline_mode():
    raise Exception("Offline mode is not supported for async migrations.")
else:
    import asyncio

    asyncio.run(run_migrations_online())
