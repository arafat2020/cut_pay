#!/bin/bash
# FastAPI Development Server Startup Script

echo "🚀 Starting FastAPI development server..."
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
