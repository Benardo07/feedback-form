# database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import ssl

DATABASE_URL = "postgresql+asyncpg://avnadmin:AVNS_naBaRsjsU2acdla9JSG@pg-7f676dd-benardo188.c.aivencloud.com:20799/feedback-form"
SSL_MODE = "require"

ssl_context = ssl.create_default_context(cafile="ca.pem")  # Adjust path as needed
if SSL_MODE == "require":
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"ssl": ssl_context}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
