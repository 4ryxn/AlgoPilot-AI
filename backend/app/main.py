from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes.auth_routes import router as auth_router
from app.routes.dashboard_routes import router as dashboard_router
from app.routes.github_routes import router as github_router
from app.routes.leetcode_routes import router as leetcode_router
from app.routes.oauth_routes import router as oauth_router
from app.routes.report_routes import router as report_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AlgoPilot-AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(leetcode_router)
app.include_router(github_router)
app.include_router(dashboard_router)
app.include_router(oauth_router)
app.include_router(report_router)

@app.get("/")
def root():
    return {"message": "AlgoPilot-AI API is running 🚀", "docs": "/docs"}
