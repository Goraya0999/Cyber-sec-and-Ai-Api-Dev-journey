import requests
#from sqlmodel import true

from App1.core.config import api_setting


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {api_setting.API_ROUTER_KEY}",
    "Content-Type": "application/json",
}

MODEL = "google/gemma-4-26b-a4b-it:free"


def chat_completion(messages: list[dict]) -> dict:
    response = requests.post(
        url=OPENROUTER_URL,
        headers=HEADERS,
        json={
            "model": MODEL,
            # "stream": True,
            "messages": messages,
            "reasoning": {
                "enabled": True
            },
        },
    )

    response.raise_for_status()

    return response.json()


    ###"google/gemma-4-26b-a4b-it:free"