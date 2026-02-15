from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
import shutil, os

from ..database import SessionLocal
from .. import models

router = APIRouter()

UPLOAD_DIR = "app/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/candidates")
def create_candidate(
    full_name: str = Form(...),
    dob: str = Form(...),
    contact_number: str = Form(...),
    address: str = Form(...),
    education: str = Form(...),
    graduation_year: int = Form(...),
    experience: float = Form(...),
    skills: str = Form(...),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    file_path = f"{UPLOAD_DIR}/{resume.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    candidate = models.Candidate(
        full_name=full_name,
        dob=dob,
        contact_number=contact_number,
        address=address,
        education=education,
        graduation_year=graduation_year,
        experience=experience,
        skills=skills,
        resume_path=file_path
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return candidate

@router.get("/candidates")
def list_candidates(
    skill: str = None,
    experience: float = None,
    graduation_year: int = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Candidate)

    if skill:
        query = query.filter(models.Candidate.skills.contains(skill))

    if experience:
        query = query.filter(models.Candidate.experience >= experience)

    if graduation_year:
        query = query.filter(
            models.Candidate.graduation_year == graduation_year
        )

    return query.all()

@router.get("/candidates/{candidate_id}")
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):
    return db.query(models.Candidate)\
             .filter(models.Candidate.id == candidate_id)\
             .first()


@router.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.query(models.Candidate)\
                  .filter(models.Candidate.id == candidate_id)\
                  .first()

    db.delete(candidate)
    db.commit()

    return {"message": "Deleted successfully"}


from fastapi import Query

@router.get("/candidates")
def search_candidates(
    skill: str | None = Query(None),
    min_experience: float | None = Query(None),
    max_experience: float | None = Query(None),
    graduation_year: int | None = Query(None),
    name: str | None = Query(None),
    db: Session = Depends(get_db)
    ):
    query = db.query(models.Candidate)

   
    if skill:
        query = query.filter(
            models.Candidate.skills.ilike(f"%{skill}%")
        )

    if min_experience is not None:
        query = query.filter(
            models.Candidate.experience >= min_experience
        )

    if max_experience is not None:
        query = query.filter(
            models.Candidate.experience <= max_experience
        )

    if graduation_year:
        query = query.filter(
            models.Candidate.graduation_year == graduation_year
        )

    if name:
        query = query.filter(
            models.Candidate.full_name.ilike(f"%{name}%")
        )

    return query.all()


