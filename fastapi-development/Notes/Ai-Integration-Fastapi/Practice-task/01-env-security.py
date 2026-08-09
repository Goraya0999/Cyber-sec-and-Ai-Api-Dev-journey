
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    openai_api_key: str
    model: str = "grok"
    debug: bool = False

    model_config = SettingsConfigDict(
        env_file=".env"
    )
        
        
@lru_cache
def get_setting() ->Settings:
    return Settings()

from fastapi import FastAPI ,Depends
app=FastAPI()
@app.get("/config")
def get_config(settings: Settings = Depends(get_setting)):
    return {
        "model": settings.model,
        "debug": settings.debug,
        "open_api_key":settings.openai_api_key
    }