from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiSettings(BaseSettings):
    API_ROUTER_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )


api_setting = ApiSettings()