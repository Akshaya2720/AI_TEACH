from pydantic import BaseModel


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


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    class_name: int
    email: str

    class Config:
        from_attributes = True