from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Student Test FastAPI B",
    description="Microservice for Student B on College Cloud CI/CD Manager",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "service": "student-test-fastapi-b",
        "student": "Student B",
        "status": "online"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }
