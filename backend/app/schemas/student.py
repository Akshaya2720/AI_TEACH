from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):#Everything inheriting from BaseModel becomes a Pydantic schema.
    name: str
    email: EmailStr
    password: str
    age: int
    class_name: int