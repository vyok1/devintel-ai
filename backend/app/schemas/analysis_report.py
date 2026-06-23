from pydantic import BaseModel

class AnalysisReportCreate(BaseModel):
    repository_id: int
    summary: str
    technologies: str
    complexity: str