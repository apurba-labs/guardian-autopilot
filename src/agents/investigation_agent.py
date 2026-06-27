import orjson

from src.models.incident import (
    Incident,
    RiskLevel,
    WorkflowState,
)
from src.prompts.investigator import SYSTEM_PROMPT
from src.services.ai.base import AIProvider


class InvestigationAgent:
    """Determines incident severity and remediation guidance."""

    def __init__(self, provider: AIProvider) -> None:
        self.provider = provider

    def run(self, incident: Incident) -> Incident:
        payload = {
            "findings": [
                finding.model_dump(mode="json")
                for finding in incident.findings
            ]
        }

        response = self.provider.chat(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=orjson.dumps(payload).decode(),
        )

        result = orjson.loads(response)

        incident.risk = RiskLevel(result["risk"])
        incident.reasoning = result["reasoning"]
        incident.recommendation = result["recommendation"]
        incident.state = WorkflowState.INVESTIGATED

        return incident