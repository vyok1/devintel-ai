from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models.repository import Repository
from app.schemas.repository import RepositoryCreate
from app.services.repository_service import create_repository
from app.models.user import Base
from app.core.database import engine, get_db
from app.schemas.user import UserCreate
from app.services.user_service import create_user
from app.services.gemini_service import analyze_repository

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "DevIntel AI Backend Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/users")
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    created_user = create_user(
        db,
        user.username,
        user.email
    )

    return {
        "id": created_user.id,
        "username": created_user.username,
        "email": created_user.email
    }
@app.post("/repositories")
def create_new_repository(
    repository: RepositoryCreate,
    db: Session = Depends(get_db)
):
    created_repository = create_repository(
        db,
        repository.github_url,
        repository.repository_name
    )

    return {
        "id": created_repository.id,
        "github_url": created_repository.github_url,
        "repository_name": created_repository.repository_name
    }
@app.get("/test-gemini")
def test_gemini():
    try:
        result = analyze_repository("FastAPI")

        return {
            "analysis": result
        }

    except Exception as e:
        return {
            "error": str(e)
        }