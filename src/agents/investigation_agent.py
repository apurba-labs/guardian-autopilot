import orjson

from src.models.incident import (
    Incident,
    RiskLevel,
    WorkflowState,
)
from src.prompts.investigator import SYSTEM_PROMPT
from src.services.ai.base import AIProvider
from src.services.memory import MemoryService
from src.services.memory.models import InvestigationRecord


class InvestigationAgent:
    """Determines incident severity and remediation guidance."""

    def __init__(self, provider: AIProvider) -> None:
        self.provider = provider
        self.memory = MemoryService()

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
        
        entities = []

        entity_groups = result.get("entities", {})
        for values in entity_groups.values():
            entities.extend(values)

        matches = self.memory.correlate(entities)
        
        record = InvestigationRecord(
            incident_id=incident.id,
            risk= RiskLevel(result["risk"]),
            decision="PENDING",
            summary=result["summary"],
            entities=entities,
        )

        incident.risk = RiskLevel(result["risk"])
        incident.reasoning = result["reasoning"]
        incident.recommendation = result["recommendation"]
        incident.state = WorkflowState.INVESTIGATED
        
        incident.metadata["summary"] = result["summary"]
        incident.metadata["entities"] = result["entities"]
        incident.metadata["memory"] = {
            "matched": len(matches) > 0,
            "count": len(matches),
            "history": matches,
        }
        
        self.memory.remember(record)
        
        return incident