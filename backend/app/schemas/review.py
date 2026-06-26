from pydantic import BaseModel


class ReviewRequest(BaseModel):
    project_path: str