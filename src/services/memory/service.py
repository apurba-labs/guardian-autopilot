from .models import InvestigationRecord
from .repository import MemoryRepository


class MemoryService:
    """Provides historical investigation correlation."""

    def __init__(self):
        self.repository = MemoryRepository()

    def remember(self, record: InvestigationRecord):
        self.repository.save(record)

    def correlate(self, entities: list[str]) -> list[dict]:
        history = self.repository.load()

        matches = []

        target = {e.lower() for e in entities}

        for incident in history:
            previous = {
                e.lower()
                for e in incident.get("entities", [])
            }

            if target.intersection(previous):
                matches.append(incident)

        return matches