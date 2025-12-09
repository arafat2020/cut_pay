# Project Structure Diagram

```mermaid
graph TD
    A[main.py - Entry Point] --> B[src/app.py - Application Factory]
    B --> C[create_app Function]
    C --> D[FastAPI Instance]
    D --> E[src/api/routes/main.py]
    D --> F[src/api/routes/health.py]

    E --> G[GET / - Root Endpoint]
    F --> H[GET /health - Health Check]

    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#fff4e1
    style D fill:#e8f5e9
    style E fill:#f3e5f5
    style F fill:#f3e5f5
    style G fill:#fce4ec
    style H fill:#fce4ec
```

## File Organization

| File                       | Purpose             | Lines of Code |
| -------------------------- | ------------------- | ------------- |
| `main.py`                  | Clean entry point   | 16            |
| `src/app.py`               | Application factory | ~18           |
| `src/api/routes/main.py`   | Root endpoint       | ~14           |
| `src/api/routes/health.py` | Health check        | ~10           |

## Benefits

✅ **Modular** - Each route is in its own file  
✅ **Scalable** - Easy to add new routes  
✅ **Clean** - main.py is minimal (16 lines)  
✅ **Testable** - Each module can be tested independently  
✅ **Professional** - Follows industry best practices
