import os
from urllib.parse import urlencode
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/oauth", tags=["OAuth"])

@router.get("/{provider}/start")
def start(provider: str):
    provider = provider.lower()
    if provider == "google":
        client = os.getenv("GOOGLE_CLIENT_ID")
        if not client: raise HTTPException(501, "Google OAuth is not configured.")
        params = urlencode({
            "client_id": client,
            "redirect_uri": "http://localhost:8000/oauth/google/callback",
            "response_type": "code",
            "scope": "openid email profile",
        })
        return {"authorization_url": f"https://accounts.google.com/o/oauth2/v2/auth?{params}"}
    if provider == "github":
        client = os.getenv("GITHUB_CLIENT_ID")
        if not client: raise HTTPException(501, "GitHub OAuth is not configured.")
        params = urlencode({
            "client_id": client,
            "redirect_uri": "http://localhost:8000/oauth/github/callback",
            "scope": "read:user user:email",
        })
        return {"authorization_url": f"https://github.com/login/oauth/authorize?{params}"}
    if provider == "linkedin":
        client = os.getenv("LINKEDIN_CLIENT_ID")
        if not client: raise HTTPException(501, "LinkedIn OAuth is not configured.")
        params = urlencode({
            "response_type": "code",
            "client_id": client,
            "redirect_uri": "http://localhost:8000/oauth/linkedin/callback",
            "scope": "openid profile email",
        })
        return {"authorization_url": f"https://www.linkedin.com/oauth/v2/authorization?{params}"}
    raise HTTPException(404, "Unsupported OAuth provider.")
