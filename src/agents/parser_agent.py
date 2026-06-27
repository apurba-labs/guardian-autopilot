from __future__ import annotations

import orjson

from src.models.incident import Incident, SecretFinding
from src.prompts.parser import SYSTEM_PROMPT
from src.services.ai.base import AIProvider


class ParserAgent:

    def __init__(self, provider: AIProvider):
        self.provider = provider
        
    def run(self, incident: Incident) -> Incident:

        response = self.provider.chat(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=incident.raw_content,
        )

        try:
            payload = orjson.loads(response)
        except orjson.JSONDecodeError:
            raise ValueError(
                "ParserAgent returned invalid JSON."
            )

        incident.findings = [
            SecretFinding(**item)
            for item in payload.get("findings", [])
        ]

        return incident