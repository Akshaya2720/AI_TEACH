from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.services.chat_service import ask_question

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/")
def chat(data: ChatRequest):

    return ask_question(data.question)