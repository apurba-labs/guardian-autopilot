from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class InvestigationRecord:
    incident_id: str
    risk: str
    decision: str
    summary: str
    entities: List[str] = field(default_factory=list)
    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )