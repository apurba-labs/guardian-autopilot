from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    qwen_api_key: str = Field(alias="QWEN_API_KEY")

    qwen_base_url: str = Field(alias="QWEN_BASE_URL")

    qwen_model: str = Field(default="qwen-plus", alias="QWEN_MODEL")

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()