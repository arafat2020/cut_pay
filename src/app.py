"""FastAPI application factory"""
from fastapi import FastAPI
from src.api.routes import health, main, highlight


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""
    app = FastAPI(
        title="FastAPI Application",
        description="A FastAPI server initialized with uv",
        version="0.1.0"
    )
    
    # Include routers
    app.include_router(main.router)
    app.include_router(health.router)
    app.include_router(highlight.router)
    
    return app
