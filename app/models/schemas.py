from pydantic import BaseModel, Field
from typing import Optional


class CodeUploadRequest(BaseModel):
    repo_url: Optional[str] = Field(..., description="Git repo URL (or local path)")
    language: str = Field(..., description="Programming language (e.g. python, kotlin)")
    generate_docs: bool = True
    generate_tests: bool = True


class JobResponse(BaseModel):
    job_id: str
    status: str
