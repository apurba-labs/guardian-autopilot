from .repository import MemoryRepository

class MemoryService:
    def __init__(self):
        self.repository = MemoryRepository()

    def remember(self, record):
        self.repository.save(record)

    def search(self, entities):
        history = self.repository.load()

        matches = []

        for incident in history:
            previous = set(incident.get("entities", []))

            if previous.intersection(entities):
                matches.append(incident)

        return matches