from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    age: int
    class_name: int


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    class_name: int

    class Config:
        from_attributes = True
class StudentLogin(BaseModel):
    email: EmailStr
    password: str