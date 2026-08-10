from fastapi import APIRouter, Depends
from app.routes.auth_routes import get_current_user
from app.services.ai_service import generate_ai_response
from app.schemas import AIRequest

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/summary")
def summary(current_user=Depends(get_current_user)):
    return {
        "user": {
            "name": current_user.name,
            "email": current_user.email,
            "leetcode_username": current_user.leetcode_username,
            "github_username": current_user.github_username,
            "linkedin_url": current_user.linkedin_url,
        }
    }

@router.post("/ai")
def ai(request: AIRequest, current_user=Depends(get_current_user)):
    return generate_ai_response(request.message, request.mode)

@router.get("/planner")
def planner(current_user=Depends(get_current_user)):
    return {"items": [
        {"title": "Two Sum", "topic": "Array / Hashing", "difficulty": "Easy", "done": False},
        {"title": "Binary Search", "topic": "Binary Search", "difficulty": "Medium", "done": False},
        {"title": "Longest Substring Without Repeating Characters", "topic": "Sliding Window", "difficulty": "Medium", "done": False},
    ]}
