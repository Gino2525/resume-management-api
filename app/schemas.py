from pydantic import BaseModel

class CandidateCreate(BaseModel):
    full_name: str
    dob: str
    contact_number: str
    address: str
    education: str
    graduation_year: int
    experience: float
    skills: str
