from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas import (
    Question,
    Student,
    StudentQuestion,
)
from app.services import (
    register_student,
    ask_ai_service,
    get_all_students,
)

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to AI Teacher"
    }


@router.get("/about")
def about():
    return {
        "project": "AI Teacher",
        "version": "1.0",
        "developer": "Akshaya"
    }


@router.get("/health")
def health():
    return {
        "status": "Server Running"
    }


@router.get("/subjects")
def subjects():
    return {
        "subjects": [
            "Mathematics",
            "Science",
            "English",
            "Social Science"
        ]
    }


@router.post("/ask")
def ask_ai(data: Question):
    return ask_ai_service(data)


@router.post("/ask_with_details")
def ask_ai_with_details(data: StudentQuestion):
    return {
        "received_question": data.question,
        "student_name": data.student_name,
        "class_name": data.class_name,
        "answer": "AI answer will come here."
    }


@router.post("/register")
def register(
    student: Student,
    db: Session = Depends(get_db)
):
    return register_student(db, student)


@router.get("/students")
def get_students(
    db: Session = Depends(get_db)
):
    return get_all_students(db)