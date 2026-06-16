from pydantic import BaseModel


class RepositoryCreate(BaseModel):
    github_url: str
    repository_name: str