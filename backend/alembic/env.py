from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import asyncio
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

# Assuming your models are defined in 'myapp/models.py' and
# you have a Base class that inherits from declarative_base()
from app.models import Base  # Update this path according to your project structure

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set the metadata object here for Alembic to access it
target_metadata = Base.metadata

def do_run_migrations(connection):
    context.configure(
        connection=connection, 
        target_metadata=target_metadata
    )

    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        echo=True,
        future=True
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

if context.is_offline_mode():
    raise Exception("Offline mode not supported with async.")
else:
    asyncio.run(run_migrations_online())
