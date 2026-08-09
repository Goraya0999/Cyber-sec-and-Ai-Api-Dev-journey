#03 Streaming chat response with StreamingResponse (FastAPI + SSE)

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import OpenAI

app = FastAPI()
client = OpenAI()  # make sure OPENAI_API_KEY is set


@app.get("/chat/stream")
async def chat_stream(message: str):
    """
    Streams AI response token-by-token using Server-Sent Events (SSE)

    Key Concepts:
    ✔ stream=True → enables chunked response
    ✔ async generator → yields data gradually
    ✔ text/event-stream → required for SSE
    """

    async def gen():
        """
        Async generator that yields response chunks
        """

        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message}],
            stream=True
        )

        for chunk in stream:
            # Extract token (delta content)
            delta = chunk.choices[0].delta.content or ""

            if delta:
                # SSE format → "data: <message>\n\n"
                yield f"data: {delta}\n\n"

        # End of stream signal
        yield "data: [DONE]\n\n"

    return StreamingResponse(
        gen(),
        media_type="text/event-stream"
    )


# =========================
# How to Test (Frontend)
# =========================

"""
1. Browser (EventSource):

const evtSource = new EventSource("http://localhost:8000/chat/stream?message=hello");

evtSource.onmessage = (event) => {
    if (event.data === "[DONE]") {
        evtSource.close();
    } else {
        console.log(event.data);  // streaming tokens
    }
};


2. Fetch API (ReadableStream):

fetch("/chat/stream?message=hello")
  .then(res => {
    const reader = res.body.getReader();
    const decoder = new TextDecoder();

    function read() {
      reader.read().then(({ done, value }) => {
        if (done) return;
        console.log(decoder.decode(value));
        read();
      });
    }

    read();
  });
"""


# =========================
# Professional Tips
# =========================

# ✔ Always send "data: ...\n\n" → required SSE format
# ✔ Use [DONE] sentinel to signal completion
# ✔ Avoid blocking operations inside generator
# ✔ For production:
#     - Add timeout handling
#     - Handle client disconnects
#     - Use async OpenAI client if available
# ✔ SSE is lightweight alternative to WebSockets for streaming APIs