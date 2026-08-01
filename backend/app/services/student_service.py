import token

from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.models.student import Student
from app.schemas.student import StudentCreate
from fastapi import HTTPException
from app.core.security import verify_password
from app.core.security import create_access_token


def create_student(db: Session, student: StudentCreate):    #StudentCreate = API object Student = Database object

    db_student = Student(
        name=student.name,
        email=student.email,
        password=hash_password(student.password),
        age=student.age,
        class_name=student.class_name
    )

    db.add(db_student) #no saving data to database until we commit the session. It is like a transaction. Until we commit the session, the data is not saved to the database.
    db.commit()
    db.refresh(db_student)

    return db_student

def login_student(db: Session, email: str, password: str):

    student = db.query(Student).filter(Student.email == email).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    print("=" * 50)
    print("Entered Email :", email)
    print("Entered Password :", password)
    print("Database Password :", repr(student.password))
    print("Type :", type(student.password))
    print("=" * 50)

    result = verify_password(password, student.password)

    print("Verification Result :", result)

    if not result:
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token(
        {
            "sub": str(student.id),
            "email": student.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }