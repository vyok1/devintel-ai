from pydantic import BaseModel


class RepositoryCreate(BaseModel):
    github_url: str
    repository_name: str
    language: str
    stars: int
class RepositoryAnalysisRequest(BaseModel):
    github_url: str  