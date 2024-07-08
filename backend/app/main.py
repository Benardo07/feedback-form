from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from .database import get_db
from .models import Feedback as DBFeedback
from .schemas import FeedbackCreate, Feedback, FeedbackOut
from typing import List
from sqlalchemy import select, desc
from .models import Feedback, Rating
from datetime import datetime
from .models import Question
from .schemas import Question as QuestionSchema
from sqlalchemy.orm import joinedload

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.post("/feedback/", response_model=FeedbackOut)
async def create_feedback(feedback_data: FeedbackCreate, db: AsyncSession = Depends(get_db)):
    async with db as session:
        try:
            # Create a new feedback entry
            new_feedback = DBFeedback(created_at=datetime.utcnow())
            session.add(new_feedback)
            await session.flush()  # Flush to assign a new ID without committing the transaction

            # Add ratings associated with the feedback
            ratings = [
                Rating(
                    score=rating.score,
                    question_id=rating.question_id,
                    feedback_id=new_feedback.id
                ) for rating in feedback_data.ratings
            ]
            session.add_all(ratings)
            
            await session.commit()
            
            # Eagerly load the ratings and their associated questions
            await session.refresh(new_feedback)
            feedback_with_ratings = await session.execute(
                select(DBFeedback)
                .options(joinedload(DBFeedback.ratings).joinedload(Rating.question))
                .filter(DBFeedback.id == new_feedback.id)
            )
            feedback = feedback_with_ratings.scalars().first()
            
            return feedback
        
        except SQLAlchemyError as e:
            await session.rollback()
            print(f"Database error: {str(e)}")
            raise HTTPException(status_code=500, detail="An error occurred while saving feedback.")
        except Exception as e:
            await session.rollback()
            print(f"General error: {str(e)}")
            raise HTTPException(status_code=500, detail="An internal error occurred.")
@app.get("/questions", response_model=List[QuestionSchema])
async def read_questions(db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(Question))
        questions = result.scalars().all()
        return questions


@app.get("/feedback/", response_model=List[FeedbackOut])
async def read_feedbacks(db: AsyncSession = Depends(get_db)):
    async with db as session:
        try:
            result = await session.execute(
                select(DBFeedback)
                .options(joinedload(DBFeedback.ratings).joinedload(Rating.question))
                .order_by(desc(DBFeedback.created_at))
            )
            feedbacks = result.unique().scalars().all()
            return feedbacks
        except SQLAlchemyError as e:
            print(f"Database error: {str(e)}")
            raise HTTPException(status_code=500, detail="An error occurred while fetching feedback.")
        except Exception as e:
            print(f"General error: {str(e)}")
            raise HTTPException(status_code=500, detail="An internal error occurred.")