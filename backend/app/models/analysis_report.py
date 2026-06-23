from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class AnalysisReport(Base):
    __tablename__ = "analysis_reports"

    id = Column(Integer, primary_key=True, index=True)
    repository_id = Column(Integer, ForeignKey("repositories.id"))
    summary = Column(String)
    technologies = Column(String)
    complexity = Column(String)