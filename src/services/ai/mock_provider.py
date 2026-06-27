import orjson

from .base import AIProvider


class MockProvider(AIProvider):
    """Offline provider used during development."""

    def chat(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.1,
    ) -> str:

        return orjson.dumps(
            {
                "findings": [
                    {
                        "type": "AWS Access Key",
                        "value": "AKIA****************",
                        "confidence": 0.99,
                        "location": "Line 4",
                    },
                    {
                        "type": "GitHub Personal Access Token",
                        "value": "ghp****************",
                        "confidence": 0.98,
                        "location": "Line 8",
                    },
                ]
            }
        ).decode()