from pydantic import BaseModel
from datetime import datetime
from typing import List

class Question(BaseModel):
    id: int
    text: str

    class Config:
        from_attributes = True

class RatingBase(BaseModel):
    score: int

class RatingCreate(RatingBase):
    question_id: int

class Rating(RatingBase):
    id: int
    question: Question

    class Config:
        from_attributes = True

class FeedbackBase(BaseModel):
    pass

class FeedbackCreate(FeedbackBase):
    ratings: List[RatingCreate]

class FeedbackOut(FeedbackBase):
    id: int
    created_at: datetime
    ratings: List[Rating]

    class Config:
        from_attributes = True

class Feedback(FeedbackBase):
    id: int
    created_at: datetime
    ratings: List[Rating]  # List of associated ratings with question details

    class Config:
        from_attributes = True

class RatingOut(BaseModel):
    id: int
    score: int
    question_id: int

    class Config:
        from_attributes = True
