from pydantic import BaseModel
from datetime import datetime

class FeedbackBase(BaseModel):
    rating: int

class FeedbackCreate(FeedbackBase):
    pass  # Only rating is required for creation

class Feedback(FeedbackBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
