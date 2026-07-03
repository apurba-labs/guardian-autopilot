import orjson

from src.models.incident import (
    DecisionType,
    Incident,
    WorkflowState,
)
from src.prompts.decision import DECISION_SYSTEM_PROMPT
from src.services.ai.base import AIProvider


class DecisionAgent:
    """Determines the operational response."""

    def __init__(self, provider: AIProvider):
        self.provider = provider

    def run(self, incident: Incident) -> Incident:
        payload = {
            "risk": incident.risk.value,
            "reasoning": incident.reasoning,
            "recommendation": incident.recommendation,
        }

        response = self.provider.chat(
            system_prompt=DECISION_SYSTEM_PROMPT,
            user_prompt=orjson.dumps(payload).decode(),
        )

        result = orjson.loads(response)

        incident.decision = DecisionType(result["decision"])
        incident.approval_required = result["approval_required"]
        incident.decision_reasoning = (
                result.get("decision_reasoning")
                or result.get("decision_reason")
                or result.get("reasoning")
                or ""
            )
        incident.state = WorkflowState.DECIDED

        return incident