# database.py
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import ssl
from dotenv import load_dotenv
from sqlalchemy.pool import NullPool

# Load environment variables from .env file
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
SSL_MODE = "require"

ssl_context = ssl.create_default_context(cafile="ca.pem")  # Adjust path as needed
if SSL_MODE == "require":
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

engine = create_async_engine(
        DATABASE_URL,
        echo=True,
        poolclass=NullPool  # Disable pooling
    )

async_session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession
)

# Using the session
async def get_db():

    async with async_session() as session:
        yield session
        