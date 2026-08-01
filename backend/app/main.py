from fastapi import FastAPI

from app.core.database import Base, engine
from app.routers.student_router import router

import app.models.student

app = FastAPI(
    title="AI Teacher API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Teacher API"
    }