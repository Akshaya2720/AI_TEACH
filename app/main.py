
from fastapi import APIRouter
from fastapi import FastAPI
from app.routes import router
from app.services import register_student

app = FastAPI()

app.include_router(router)
router = APIRouter()
students = []
@router.get("/")
def home():
    return{
        "message":"Welcome to AI Teacher"
    }
@router.get("/about")
def about():
    return{
        "project":"AI Teacher",
        "version":"1.0",
        "developer":"Akshaya"
    }
@router.get("/health")
def health():
    return{
        "status":"Server Running"
    }
@router.get("/subjects")
def subjects():
    return{
    "subjects": [
            "Mathematics",
            "Science",
            "English",
            "Social Science"
        ]
    }

from pydantic import BaseModel
class Question(BaseModel):
    question: str

@router.post("/ask")
def ask_ai(data:Question):
    return{
        "received_question":data.question,
        "answer":"AI answer will come here."
    }
@router.post("/ask_with_details")
def ask_ai_with_details(data: dict):
    return{
        "received_question": data.question,
        "student_name": data.student_name,
        "class_name": data.class_name,
        "answer": "AI answer will come here."
    }
class Student(BaseModel):
    name: str
    age: int
    class_name: int
    email: str
@router.post("/register")
def register(student: Student):
    return register_student(student)

@router.get("/students")
def get_students():
    return students