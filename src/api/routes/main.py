"""Main application routes"""
from fastapi import APIRouter

router = APIRouter(tags=["main"])


@router.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to FastAPI!",
        "status": "running",
        "docs": "/docs"
    }
