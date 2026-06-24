from sqlalchemy.orm import Session

from app.models.repository import Repository


def create_repository(
    db: Session,
    github_url: str,
    repository_name: str,
    language: str,
    stars: int
):
    repository = Repository(
        github_url=github_url,
        repository_name=repository_name,
        language=language,
        stars=stars
    )

    db.add(repository)
    db.commit()
    db.refresh(repository)

    return repository
