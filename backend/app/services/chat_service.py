from app.llm.provider import LLMProvider

from app.memory.conversation import (
    add_user_message,
    add_assistant_message,
    get_conversation
)


def ask_question(question: str):

    add_user_message(question)

    messages = get_conversation()

    answer = LLMProvider.generate(messages)

    add_assistant_message(answer)

    return {
        "answer": answer
    }