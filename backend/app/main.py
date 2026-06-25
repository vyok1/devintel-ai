from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models.repository import Repository
from app.schemas.repository import RepositoryCreate
from app.services.repository_service import create_repository
from app.core.database import Base
from app.core.database import engine, get_db
from app.schemas.user import UserCreate
from app.services.user_service import create_user
from app.services.gemini_service import analyze_repository
from app.models.analysis_report import AnalysisReport
from app.schemas.analysis_report import AnalysisReportCreate

from app.services.github_service import (
    get_repository_info,
    extract_repo_info
)

from app.schemas.repository import RepositoryAnalysisRequest


from app.services.analysis_service import (
    generate_analysis,
    save_analysis
)
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
        repository.repository_name,
        repository.language,
        repository.stars
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
@app.post("/analyze-repository")
def analyze_repository(
    request: RepositoryAnalysisRequest,
    db: Session = Depends(get_db)
):

    owner, repo = extract_repo_info(
        request.github_url
    )

    repo_info = get_repository_info(
        owner,
        repo
    )
    created_repository = create_repository(
    db,
    request.github_url,
    repo_info["name"],
    repo_info["language"],
    repo_info["stars"]
)

    analysis = generate_analysis(repo_info)

    saved_report = save_analysis(
    db,
    repository_id=created_repository.id,
    analysis=analysis
)

    return {
        "repository": repo_info,
        "analysis": analysis,
        "saved_report_id": saved_report.id
    }