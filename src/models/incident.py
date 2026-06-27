from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class RiskLevel(str, Enum):
    """Incident severity."""

    UNKNOWN = "UNKNOWN"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class WorkflowState(str, Enum):
    """Pipeline state."""

    RECEIVED = "RECEIVED"
    PARSED = "PARSED"
    INVESTIGATED = "INVESTIGATED"
    DECIDED = "DECIDED"
    APPROVED = "APPROVED"
    COMPLETED = "COMPLETED"

class FindingSeverity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class SecretFinding(BaseModel):
    """Represents a detected secret or credential."""

    type: str
    provider: str | None = None
    value: str
    confidence: float
    location: str | None = None
    severity: FindingSeverity = FindingSeverity.HIGH
    description: str | None = None


class Incident(BaseModel):
    """Main workflow object shared across every agent."""

    id: str
    source: str
    raw_content: str
    findings: list[SecretFinding] = Field(default_factory=list)
    risk: RiskLevel = RiskLevel.LOW
    reasoning: str = ""
    recommendation: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
    state: WorkflowState = WorkflowState.RECEIVED
    created_at: datetime = Field(default_factory=datetime.utcnow)