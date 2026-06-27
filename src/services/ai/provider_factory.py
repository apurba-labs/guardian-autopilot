import os

from .mock_provider import MockProvider
from .qwen_provider import QwenProvider


def get_provider():

    if os.getenv("QWEN_API_KEY"):
        return QwenProvider()

    return MockProvider()