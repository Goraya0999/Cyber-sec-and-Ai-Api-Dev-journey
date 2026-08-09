# ==========================================================
# #02 POST /chat — Basic AI Chat Completion Endpoint
# ==========================================================

# Goal:
# Build a FastAPI endpoint that:
# 1. Receives a user message
# 2. Sends the message to an AI model
# 3. Receives the AI response
# 4. Returns the reply to the client
#
# Request Flow:
#
# Client
#   |
#   | POST /chat
#   v
# FastAPI
#   |
#   | Call AI API
#   v
# Grok / OpenAI
#   |
#   | Generate response
#   v
# FastAPI
#   |
#   | Return JSON
#   v
# Client


# ==========================================================
# STEP 1: Imports
# ==========================================================

from fastapi import FastAPI
from pydantic import BaseModel

# OpenAI SDK works with Grok too
# when configured correctly.

from openai import OpenAI


# ==========================================================
# STEP 2: Create FastAPI App
# ==========================================================

app = FastAPI()


# ==========================================================
# STEP 3: Create AI Client
# ==========================================================

# Never hardcode API keys!

client = OpenAI(
    api_key="YOUR_API_KEY"
)

# Better approach:
#
# api_key = settings.openai_api_key
#
# Loaded from .env file


# ==========================================================
# STEP 4: Request Model
# ==========================================================

class ChatRequest(BaseModel):
    """
    Data sent by user.

    Example:

    {
        "message": "Hello",
        "model": "grok-3"
    }
    """

    message: str

    # default model

    model: str = "grok-3"


# ==========================================================
# STEP 5: Response Model
# ==========================================================

class ChatResponse(BaseModel):
    """
    Data returned to user.

    Example:

    {
        "reply": "Hello! How can I help?",
        "model": "grok-3",
        "tokens_used": 25
    }
    """

    reply: str

    model: str

    tokens_used: int


# ==========================================================
# STEP 6: Create POST Endpoint
# ==========================================================

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):

    """
    req contains:

    ChatRequest(
        message="Hello",
        model="grok-3"
    )
    """

    # Send request to AI

    response = client.chat.completions.create(

        model=req.model,

        messages=[
            {
                "role": "user",
                "content": req.message
            }
        ]
    )

    # Extract generated text

    ai_reply = response.choices[0].message.content

    # Return structured response

    return ChatResponse(
        reply=ai_reply,
        model=response.model,
        tokens_used=response.usage.total_tokens
    )


# ==========================================================
# Example Request
# ==========================================================

"""
POST /chat

{
    "message": "What is Python?"
}
"""


# ==========================================================
# Example Response
# ==========================================================

"""
{
    "reply": "Python is a programming language.",
    "model": "grok-3",
    "tokens_used": 34
}
"""