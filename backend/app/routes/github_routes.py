from fastapi import APIRouter, Depends, HTTPException
from app.routes.auth_routes import get_current_user
from app.services.github_service import fetch_github

router = APIRouter(prefix="/github", tags=["GitHub"])

@router.get("/profile")
def profile(current_user=Depends(get_current_user)):
    if not current_user.github_username:
        raise HTTPException(400, "Add a GitHub username first.")
    try:
        return fetch_github(current_user.github_username)
    except Exception as exc:
        raise HTTPException(502, f"Unable to fetch GitHub profile: {exc}")
