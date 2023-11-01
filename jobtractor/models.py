from pydantic import BaseModel
from typing import Optional, Sequence
from datetime import datetime

class JobData(BaseModel):
    job_name: str
    job_location: str
    job_required_years_work_experience: Optional[int]

class JobMeta(BaseModel):
    company_job_id: str
    html: str
    url : str
    extracted_at : datetime

class Organization(BaseModel):
    career_url: str
    jobs_url: str
    jobs_base_url: Optional[str]
    career_forward_url: Optional[str]
    id_extract_re: str

class JobObject(BaseModel):
    data : JobData
    meta : JobMeta


class JobObjects(BaseModel):
    jobs: Sequence[JobObject]