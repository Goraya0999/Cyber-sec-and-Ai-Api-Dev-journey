from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi.responses import StreamingResponse
app=FastAPI(
    title="MY API"
)

class Settings(BaseSettings):
    grok_api_key: str
    model: str = "llama-3.3-70b-versatile"

    model_config = SettingsConfigDict(
        env_file=".env"
    )

settings = Settings()

client=OpenAI(
    api_key=settings.grok_api_key,
    base_url="https://api.groq.com/openai/v1"
)

class ChatRequest(BaseModel):
    message:str
    model: str = "llama-3.3-70b-versatile"
    
class ChatResponse(BaseModel):
    reply:str
    model:str
    token_used:int
@app.post("/chat",response_model=ChatResponse)
async def chat(req:ChatRequest):
    response=client.chat.completions.create(
        model=req.model,
        messages=[
            {
                "role":"user",
                "content":req.message
            }
        ]
    )
    
    ai_reply=response.choices[0].message.content
    return ChatResponse(
        reply=ai_reply,
        model=response.model,
        token_used=response.usage.total_tokens
    )
    
@app.get("/chat/stream")
async def chat_stream(message: str, model: str = "llama-3.3-70b-versatile"):

    async def gen():
        stream = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ],
            stream=True
        )

        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""

            if delta:
                yield f"data: {delta}\n\n"

        # End signal
        yield "data: [DONE]\n\n"

    return StreamingResponse(gen(), media_type="text/event-stream")