from fastapi import APIRouter, Depends, HTTPException
from app.routes.auth_routes import get_current_user

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/pdf")
def pdf(current_user=Depends(get_current_user)):
    raise HTTPException(
        501,
        "PDF generation placeholder. Add reportlab in the deployment/report phase."
    )
