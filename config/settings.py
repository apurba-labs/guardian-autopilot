from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    api_url: str = Field(
        default="http://127.0.0.1:8000/api/v1/scan",
        alias="API_URL",
    )
    dashscope_api_key: str = Field(alias="DASHSCOPE_API_KEY")

    qwen_base_url: str = Field(alias="QWEN_BASE_URL")

    qwen_model: str = Field(default="qwen3.7-plus", alias="QWEN_MODEL")

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()