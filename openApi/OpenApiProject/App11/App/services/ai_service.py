from App1.clients.openrouter_client import chat_completion

from App1.services.system_prompot import SYSTEM_PROMPT


def ask_ai(question: str) -> dict:

    messages = [
        {
                    "role": "system",
                    "content": """
        Answer clearly and concisely.
        Use plain text only.
        Do not use Markdown formatting.
        Do not use unnecessary symbols.
        Use emojis to make the answer more engaging.
        And Also used Relevant emojis to make the answer more engaging.
        """,
                },
       
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": question,
        }
    ]

    response = chat_completion(messages)

    return response["choices"][0]["message"]