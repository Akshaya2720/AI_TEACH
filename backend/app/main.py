from fastapi import FastAPI
from app.routers.chat_router import router as chat_router
from app.core.database import Base, engine
from app.routers.student_router import router
from app.routers.chat_router import router as chat_router
import app.models.student
from app.routers.student_router import router as student_router
app = FastAPI(
    title="AI Teacher API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(student_router)
app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Teacher API"
    }