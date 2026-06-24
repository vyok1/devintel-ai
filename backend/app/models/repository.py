from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)

    github_url = Column(String, nullable=False)

    repository_name = Column(String, nullable=False)
    language = Column(String)
    stars = Column(Integer)