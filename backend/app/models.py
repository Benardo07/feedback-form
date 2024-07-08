# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Feedback(Base):
    __tablename__ = 'feedbacks'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    ratings = relationship("Rating", back_populates="feedback", cascade="all, delete")

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    ratings = relationship("Rating", back_populates="question", cascade="all, delete")

class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)
    feedback_id = Column(Integer, ForeignKey('feedbacks.id'), nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    feedback = relationship("Feedback", back_populates="ratings")
    question = relationship("Question", back_populates="ratings")