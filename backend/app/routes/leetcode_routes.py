from fastapi import APIRouter, Depends, HTTPException, Query
from app.routes.auth_routes import get_current_user
from app.services.leetcode_service import fetch_profile, fetch_calendar

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
    except Exception as exc:
        raise HTTPException(502, f"Unable to fetch LeetCode profile: {exc}")

@router.get("/calendar")
def calendar(year: int | None = Query(default=None), current_user=Depends(get_current_user)):
    if not current_user.leetcode_username:
        raise HTTPException(400, "Add a LeetCode username first.")
    try:
        return fetch_calendar(current_user.leetcode_username, year)
    except Exception as exc:
        raise HTTPException(502, f"Unable to fetch LeetCode calendar: {exc}")
