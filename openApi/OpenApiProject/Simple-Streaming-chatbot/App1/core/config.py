from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiSettings(BaseSettings):
    # Required — app refuses to start without it (fails fast, no silent None key)
    API_ROUTER_KEY: str = Field(..., description="OpenRouter API key")

    # Configurable instead of hardcoded, with sensible defaults
    OPENROUTER_MODEL: str = "google/gemma-4-26b-a4b-it:free"
    OPENROUTER_URL: str = "https://openrouter.ai/api/v1/chat/completions"
    REQUEST_TIMEOUT: float = 30.0  # seconds — never make an unbounded network call

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )


# Loaded once, reused everywhere — avoids re-reading .env on every call
api_setting = ApiSettings()
