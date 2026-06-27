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
        
        if "Guardian Investigation Agent" in system_prompt:
            return orjson.dumps(
                {
                    "risk": "CRITICAL",
                    "reasoning": (
                        "Production AWS credentials and GitHub Personal "
                        "Access Token were exposed."
                    ),
                    "recommendation": [
                        "Rotate AWS credentials",
                        "Revoke GitHub Personal Access Token",
                        "Review audit logs",
                        "Notify Security Team",
                    ],
                }
            ).decode()

        return orjson.dumps(
            {
                "findings": [
                    {
                        "type": "AWS Access Key",
                        "provider":"AWS",
                        "severity":"Critical",
                        "description":"Production credential exposed",
                        "value": "AKIA****************",
                        "confidence": 0.99,
                        "location": "Line 4",
                    },
                    {
                        "type": "GitHub Personal Access Token",
                        "provider":"GitHub",
                        "severity":"Critical",
                        "description":"Production credential exposed",
                        "value": "ghp****************",
                        "confidence": 0.98,
                        "location": "Line 8",
                    },
                ]
            }
        ).decode()