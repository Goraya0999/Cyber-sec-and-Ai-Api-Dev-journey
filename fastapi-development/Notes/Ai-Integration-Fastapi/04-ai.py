#04 Multi-turn conversation history endpoint (Stateful Chat API)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from openai import OpenAI

app = FastAPI()
client = OpenAI()

# In-memory storage for conversations
conversations: Dict[str, List[dict]] = {}

# Limit history to avoid token overflow
MAX_HISTORY = 20


class ChatRequest(BaseModel):
    message: str


@app.post("/chat/{session_id}")
def chat(session_id: str, req: ChatRequest):
    """
    Handles multi-turn conversation using session_id.

    Flow:
    1. Get existing history (or create new)
    2. Append user message
    3. Send full history to OpenAI
    4. Append assistant reply
    5. Trim history if too long
    """

    # Get or create session history
    history = conversations.setdefault(session_id, [])

    # Add user message
    history.append({
        "role": "user",
        "content": req.message
    })

    # Trim old messages (keep last MAX_HISTORY)
    if len(history) > MAX_HISTORY:
        history[:] = history[-MAX_HISTORY:]

    # Call OpenAI with full conversation
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=history
    )

    reply = resp.choices[0].message.content

    # Add assistant reply
    history.append({
        "role": "assistant",
        "content": reply
    })

    return {
        "reply": reply,
        "turns": len(history) // 2
    }


@app.get("/chat/{session_id}/history")
def get_history(session_id: str):
    """
    Returns full conversation history for a session
    """

    history = conversations.get(session_id)

    if history is None:
        raise HTTPException(status_code=404, detail="Session not found")

    return {
        "session_id": session_id,
        "history": history
    }


@app.delete("/chat/{session_id}")
def clear_session(session_id: str):
    """
    Deletes a session (clears chat history)
    """

    if session_id in conversations:
        del conversations[session_id]
        return {"status": "deleted"}

    raise HTTPException(status_code=404, detail="Session not found")


# =========================
# Example Usage
# =========================

"""
POST /chat/abc123
{
    "message": "Hello"
}

POST /chat/abc123
{
    "message": "What did I just say?"
}

GET /chat/abc123/history

DELETE /chat/abc123
"""


# =========================
# Professional Tips
# =========================

# ✔ In-memory dict is NOT persistent → resets on server restart
# ✔ For production:
#     - Use Redis / Database for session storage
#     - Add TTL (auto-expire sessions)
# ✔ Always limit history (token + cost control)
# ✔ Consider storing only last N messages or summaries
# ✔ Add user authentication for secure session handling