from pydantic import BaseModel

class ScanRequest(BaseModel):
    source: str = "api"
    content: str

class MemoryHistoryItem(BaseModel):
    incident_id: str
    risk: str
    decision: str
    summary: str
    entities: list[str]
    created_at: str


class MemoryResponse(BaseModel):
    matched: bool
    count: int
    history: list[MemoryHistoryItem] = []


class ReportResponse(BaseModel):
    title: str
    summary: str
    content: str


class ScanResponse(BaseModel):
    incident_id: str
    state: str
    risk: str
    decision: str | None = None
    memory: MemoryResponse | None = None
    report: ReportResponse