from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.student import StudentCreate
from app.services.student_service import create_student


#Instead of putting every endpoint inside main.py, we organize related endpoints together
router = APIRouter(
    prefix="/students",
    tags=["Students"]#This only affects the Swagger documentation. Your endpoints will appear under a Students section.
)


@router.post("/register")
def register_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return create_student(db, student)