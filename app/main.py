from fastapi import FastAPI
app=FastAPI()
students = []
@app.get("/")
def home():
    return{
        "message":"Welcome to AI Teacher"
    }
@app.get("/about")
def about():
    return{
        "project":"AI Teacher",
        "version":"1.0",
        "developer":"Akshaya"
    }
@app.get("/health")
def health():
    return{
        "status":"Server Running"
    }
@app.get("/subjects")
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

@app.post("/ask")
def ask_ai(data:Question):
    return{
        "received_question":data.question,
        "answer":"AI answer will come here."
    }
@app.post("/ask_with_details")
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

@app.post("/register")
def register(student: Student):
    students.append(student)

    return {
        "message": "Student Registered Successfully",
        "student": student
    }

@app.get("/students")
def get_students():
    return students