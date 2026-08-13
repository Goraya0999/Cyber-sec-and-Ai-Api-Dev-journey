from typing import Generator

from App1.clients.openrouter_client import chat_completion, chat_completion_stream
from App1.services.system_prompt import SYSTEM_PROMPT

STYLE_PROMPT = """
Answer clearly and concisely.
Use plain text only.
Do not use Markdown formatting.
Do not use unnecessary symbols like asterisks or underscores or #.
Use relevant emojis to make the answer more engaging.
"""

MAX_QUESTION_LENGTH = 4000  # basic input validation / abuse guard


def _build_messages(question: str) -> list[dict]:
    # Input validation: reject empty or absurdly long input before it ever
    # reaches the network call. Cheap way to avoid wasted API spend/abuse.
    question = question.strip()
    if not question:
        raise ValueError("Question must not be empty")
    if len(question) > MAX_QUESTION_LENGTH:
        raise ValueError(f"Question too long (max {MAX_QUESTION_LENGTH} chars)")

    return [
        {"role": "system", "content": STYLE_PROMPT},
       
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]


def ask_ai(question: str) -> dict:
    """Non-streaming: returns the full message dict once the answer is ready."""
    messages = _build_messages(question)
    response = chat_completion(messages)
    return response["choices"][0]["message"]


def ask_ai_stream(question: str) -> Generator[str, None, None]:
    """Streaming: yields text chunks as the model generates them."""
    messages = _build_messages(question)
    yield from chat_completion_stream(messages)
