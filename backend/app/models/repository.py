from sqlalchemy import Column, Integer, String

from app.models.user import Base


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)

    github_url = Column(String, nullable=False)

    repository_name = Column(String, nullable=False)