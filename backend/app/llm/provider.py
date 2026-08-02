from openai import OpenAI
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.core.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_BASE_URL,
    MODEL_NAME,
)

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
)


class LLMProvider:

    @staticmethod
    def generate(messages: list):

        try:

            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages = [
                        {
                            "role": "system",
                            "content": SYSTEM_PROMPT
                        }
                    ] + messages
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"LLM Error: {str(e)}"