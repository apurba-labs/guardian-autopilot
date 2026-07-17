import json
from pathlib import Path

from .models import InvestigationRecord


class MemoryRepository:
    """Persists investigation history for incident correlation."""

    def __init__(self, path: str = "data/investigations.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            self.path.write_text("[]")

    def load(self) -> list[dict]:
        return json.loads(self.path.read_text())

    def save(self, record: InvestigationRecord) -> None:
        history = self.load()
        history.append(record.__dict__)

        self.path.write_text(
            json.dumps(history, indent=2)
        )