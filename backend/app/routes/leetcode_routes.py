from fastapi import APIRouter, Depends, HTTPException, Query
from app.routes.auth_routes import get_current_user
from app.services.leetcode_service import (
    LeetCodeUnavailable,
    LeetCodeUserNotFound,
    fetch_calendar,
    fetch_profile,
)

router = APIRouter(prefix="/leetcode", tags=["LeetCode"])

@router.get("/profile")
def profile(current_user=Depends(get_current_user)):
    if not current_user.leetcode_username:
        raise HTTPException(400, "Add a LeetCode username first.")
    try:
        data = fetch_profile(current_user.leetcode_username)
        return {
            "username": current_user.leetcode_username,
            "profile": data.get("profile"),
            "stats": data.get("submitStatsGlobal"),
        }
    except LeetCodeUserNotFound:
        raise HTTPException(404, "LeetCode user not found.")
    except LeetCodeUnavailable as exc:
        raise HTTPException(503, str(exc))

@router.get("/calendar")
def calendar(year: int | None = Query(default=None), current_user=Depends(get_current_user)):
    if not current_user.leetcode_username:
        raise HTTPException(400, "Add a LeetCode username first.")
    try:
        return fetch_calendar(current_user.leetcode_username, year)
    except LeetCodeUserNotFound:
        raise HTTPException(404, "LeetCode user not found.")
    except LeetCodeUnavailable as exc:
        raise HTTPException(503, str(exc))
