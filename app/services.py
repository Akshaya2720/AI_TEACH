from sqlalchemy.orm import Session

from app.models import Student
from app.schemas import Student as StudentSchema


def register_student(db: Session, student: StudentSchema):

    db_student = Student(
        name=student.name,
        age=student.age,
        class_name=student.class_name,
        email=student.email
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return {
        "message": "Student Registered Successfully",
        "student": db_student
    }


def get_all_students(db: Session):
    return db.query(Student).all()


def ask_ai_service(data):
    return {
        "question": data.question,
        "answer": "AI answer will come here"
    }