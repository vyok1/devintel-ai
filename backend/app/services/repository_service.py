from sqlalchemy.orm import Session

from app.models.repository import Repository


def create_repository(
    db: Session,
    github_url: str,
    repository_name: str
):
    repository = Repository(
        github_url=github_url,
        repository_name=repository_name
    )

    db.add(repository)
    db.commit()
    db.refresh(repository)

    return repository