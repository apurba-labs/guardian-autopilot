from uuid import uuid4

from fastapi import APIRouter

from src.api.schemas import ScanRequest, ScanResponse
from src.core.orchestrator import GuardianOrchestrator
from src.models.incident import Incident
from src.services.ai.provider_factory import get_provider

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "guardian-autopilot",
    }
    
    
@router.post("/api/v1/scan", response_model=ScanResponse)
def scan(request: ScanRequest):

    incident = Incident(
        id=str(uuid4()),
        source=request.source,
        raw_content=request.content,
    )

    workflow = GuardianOrchestrator(
        get_provider()
    )

    incident = workflow.run(incident)

    return ScanResponse(
        incident_id=incident.id,
        state=incident.state.value,
        risk=incident.risk.value,
        decision=incident.decision.value if incident.decision else None,
        memory=incident.metadata.get("memory"),
        report=incident.metadata["report"],
    )