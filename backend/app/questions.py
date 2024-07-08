from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from models import Base, Question

# Define the async engine and sessionmaker
DATABASE_URL = "postgresql+asyncpg://avnadmin:AVNS_naBaRsjsU2acdla9JSG@pg-7f676dd-benardo188.c.aivencloud.com:20799/feedback-form"
engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def add_initial_questions():
    async with AsyncSessionLocal() as session:
        questions = [
            "How would you rate your overall satisfaction with our product?",
            "How do you rate the quality of our product?",
            "How satisfied are you with the value for money of our product?",
            "How well does our product meet your needs?",
            "How likely are you to recommend our product to others?",
            "How satisfied are you with the customer support for our product?",
            "How likely are you to purchase other products from us in the future?"
        ]
        # Check if questions already exist to prevent duplication
        existing_questions = await session.execute(select(Question))
        existing_texts = {q.text for q in existing_questions.scalars()}
        new_questions = [Question(text=q_text) for q_text in questions if q_text not in existing_texts]
        session.add_all(new_questions)
        await session.commit()

if __name__ == "__main__":
    import asyncio
    asyncio.run(add_initial_questions())
