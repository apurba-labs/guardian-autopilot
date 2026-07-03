from config.settings import get_settings

from .mock_provider import MockProvider
from .qwen_provider import QwenProvider


def get_provider():
    settings = get_settings()

    if settings.dashscope_api_key:
        return QwenProvider()

    return MockProvider()