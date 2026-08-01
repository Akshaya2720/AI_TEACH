from sqlalchemy.orm import Session

from app.models.student import Student
from app.schemas.student import StudentCreate


def create_student(db: Session, student: StudentCreate):    #StudentCreate = API object Student = Database object

    db_student = Student(
        name=student.name,
        email=student.email,
        password=student.password,
        age=student.age,
        class_name=student.class_name
    )

    db.add(db_student) #no saving data to database until we commit the session. It is like a transaction. Until we commit the session, the data is not saved to the database.
    db.commit()
    db.refresh(db_student)

    return db_student