# FastAPI

* [FastAPI Docs](https://fastapi.tiangolo.com/)

### 1. Installation
```bash
pip install fastapi
pip install "uvicorn[standard]"

uvicorn main:app --reload  # Default
uvicorn main:app --host 127.0.0.1 --port 80 --reload  # Localhost
uvicorn main:app --host 0.0.0.0 --port 8000 --reload  # Docker
```

* [http://localhost:8000/docs](http://localhost:8000/docs) - Swagger documentation
* [http://localhost:8000/redoc](http://localhost:8000/redoc) - Alternative docs by ReDoc
