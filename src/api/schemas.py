from pydantic import BaseModel

class ScanRequest(BaseModel):
    source: str = "api"
    content: str


class ScanResponse(BaseModel):
    incident_id: str
    state: str
    risk: str
    decision: str | None = None
    report: dict