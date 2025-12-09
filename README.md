# FastAPI Application

A FastAPI server initialized with `uv` package manager.

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) package manager

## Installation

This project uses `uv` for dependency management. Dependencies are already configured in `pyproject.toml`.

To install dependencies:

```bash
uv sync
```

## Running the Server

### Method 1: Using the start script (Recommended)

```bash
./start.sh
```

### Method 2: Using Python directly

```bash
uv run python main.py
```

### Method 3: Using uvicorn directly

```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

> **Note**: The `start.sh` script is a convenient wrapper that runs uvicorn with hot-reload enabled.

## API Endpoints

Once the server is running, you can access:

- **Root**: http://localhost:8000/
- **Health Check**: http://localhost:8000/health
- **Interactive API Docs (Swagger)**: http://localhost:8000/docs
- **Alternative API Docs (ReDoc)**: http://localhost:8000/redoc

## Project Structure

```
.
├── main.py              # Clean entry point
├── src/
│   ├── __init__.py
│   ├── app.py          # Application factory
│   └── api/
│       ├── __init__.py
│       └── routes/
│           ├── __init__.py
│           ├── main.py      # Root endpoint
│           └── health.py    # Health check endpoint
├── pyproject.toml       # Project configuration and dependencies
├── .env.example         # Environment variables example
└── README.md           # This file
```

## Development

The server runs with auto-reload enabled by default when using the uvicorn command with `--reload` flag.

## Environment Variables

Copy `.env.example` to `.env` and modify as needed:

```bash
cp .env.example .env
```
