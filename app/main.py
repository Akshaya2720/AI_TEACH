from fastapi import FastAPI

from app.core.database import Base, engine
from app.routes import router
import app.models

app = FastAPI(
    title="AI Teacher API",
    version="1.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)