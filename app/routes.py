from fastapi import APIRouter
from app.schemas import Question, Student
from app.database import students
from app.services import ask_ai_service, get_all_students
from app.services import register_student
from app.services import ask_ai_service

router = APIRouter()


@router.post("/register")
def register(student: Student):
    return register_student(student)


@router.post("/ask")
def ask_ai(data: Question):
    return ask_ai_service(data)


@router.get("/students")
def get_students():
    return get_all_students()

