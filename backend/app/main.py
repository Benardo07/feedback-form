from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from .models import Feedback as DBFeedback
from .schemas import FeedbackCreate, Feedback
from typing import List
from sqlalchemy import select

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/feedback/", response_model=Feedback)
async def create_feedback(feedback: FeedbackCreate, db: AsyncSession = Depends(get_db)):
    db_feedback = DBFeedback(rating=feedback.rating)  # DBFeedback should match your SQLAlchemy model
    db.add(db_feedback)
    await db.commit()
    await db.refresh(db_feedback)
    return db_feedback

@app.get("/feedback/", response_model=List[Feedback])
async def read_feedbacks(db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(DBFeedback))
        feedbacks = result.scalars().all()
        return feedbacks