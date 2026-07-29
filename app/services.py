from app.database import students

def register_student(student):
    students.append(student)

    return {
        "message": "Student Registered Successfully",
        "student": student
    }
def ask_ai_service(data):

    return {
        "question": data.question,
        "answer": "AI answer will come here"
    }
def get_all_students():
    return students