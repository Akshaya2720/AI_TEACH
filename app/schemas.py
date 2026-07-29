from pydantic import BaseModel
from app.schemas import Student
class Question(BaseModel):
    question: str


class StudentQuestion(BaseModel):
    question: str
    student_name: str
    class_name: int


class Student(BaseModel):
    name: str
    age: int
    class_name: int
    email: str