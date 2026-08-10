from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    leetcode_username = Column(String(120), nullable=True)
    linkedin_url = Column(String(500), nullable=True)
    github_username = Column(String(120), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
