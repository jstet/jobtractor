from pydantic import BaseModel
from typing import Optional, Sequence

class Job(BaseModel):
    job_name: str
    job_location: str
    job_required_years_work_experience: Optional[int]

class Jobs(BaseModel):
    jobs: Sequence[Job]