from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- Core services ---
    DATABASE_URL: str
    REDIS_URL: str

    # --- JWT / auth ---
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # --- Account lockout ---
    MAX_FAILED_LOGIN_ATTEMPTS: int = 5
    LOCKOUT_DURATION_MINUTES: int = 15

    # --- Rate limiting ---
    # Kept higher than MAX_FAILED_LOGIN_ATTEMPTS: rate limiting guards against
    # rapid-fire brute force / DoS, while account lockout is the tighter,
    # per-account control. If these two thresholds collide, a legitimate
    # "is this account now locked?" check can get masked by a 429 instead.
    LOGIN_RATE_LIMIT: str = "10/minute"
    REGISTER_RATE_LIMIT: str = "3/hour"
    DEFAULT_RATE_LIMIT: str = "100/minute"
    # Defaults to REDIS_URL in production; tests point this at "memory://"
    # so the suite doesn't need a real Redis server just to exercise limits.
    RATE_LIMIT_STORAGE_URI: str | None = None

    # --- App / environment ---
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    CORS_ORIGINS: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()]


settings = Settings()
