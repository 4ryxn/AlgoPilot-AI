from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    leetcode_username: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_username: Optional[str] = None

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    email: EmailStr
    leetcode_username: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_username: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class AIRequest(BaseModel):
    message: str
    mode: str = "coach"
