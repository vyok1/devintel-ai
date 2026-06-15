from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.models.user import Base
from app.core.database import engine, get_db
from app.schemas.user import UserCreate
from app.services.user_service import create_user

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