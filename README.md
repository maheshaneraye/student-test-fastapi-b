# Student Test FastAPI B

A lightweight Python + FastAPI microservice created for College Cloud CI/CD Manager integration and multi-tenant testing.

## Service Specification
- **Student Owner:** Student B
- **Runtime:** Python 3.11 / FastAPI
- **Container Port:** `8000`
- **Assigned Public Port:** `8022`

## API Endpoints
- `GET /` — Returns service metadata JSON:
  ```json
  {
    "service": "student-test-fastapi-b",
    "student": "Student B",
    "status": "online"
  }
  ```
- `GET /health` — Returns health probe JSON:
  ```json
  {
    "status": "ok"
  }
  ```

## Local Development & Testing
```bash
# Install dependencies
pip install -r requirements.txt

# Run pytest test suite
pytest -v

# Run FastAPI app locally
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Docker Build
```bash
docker build -t student-test-fastapi-b .
docker run -p 8000:8000 student-test-fastapi-b
```
