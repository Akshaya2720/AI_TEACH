from fastapi import FastAPI

from app.core.database import Base, engine

import app.models.student


#creates the application
app = FastAPI(
    title="AI Teacher API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)
#Create every table registered in metadata if it doesn't already exist.

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Teacher API"
    }