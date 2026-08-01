from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user
from app.core.database import get_db
from app.schemas.student import StudentCreate, StudentResponse
from app.services.student_service import create_student

from app.schemas.student import (
    StudentLogin
)

from app.services.student_service import (
    create_student,
    login_student
)


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post(
    "/register",
    response_model=StudentResponse
)
def register_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return create_student(db, student)

@router.post("/login")
def login(
    data: StudentLogin,
    db: Session = Depends(get_db)
):
    return login_student(
        db,
        data.email,
        data.password
    )

@router.get("/profile")
def profile(
    current_user=Depends(get_current_user)
):

    return {
        "message": "Protected Route",
        "user": current_user
    }