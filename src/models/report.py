from pydantic import BaseModel

class IncidentReport(BaseModel):
    """Human-readable incident report."""

    title: str
    summary: str
    content: str