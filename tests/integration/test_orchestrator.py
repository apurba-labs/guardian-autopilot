from pathlib import Path
from uuid import uuid4

from rich.console import Console

from src.core.orchestrator import GuardianOrchestrator
from src.models.incident import Incident
from src.services.ai.provider_factory import get_provider

console = Console()


def main() -> None:
    incident = Incident(
        id=str(uuid4()),
        source="fixture",
        raw_content=Path(
            "fixtures/incidents/mixed_incident.txt"
        ).read_text(encoding="utf-8"),
    )
    
    provider = get_provider()
    workflow = GuardianOrchestrator(provider)
    incident = workflow.run(incident)

    report = incident.metadata["report"]
    console.rule("[bold green]Guardian Autopilot")
    console.print(report["title"])
    console.print()
    console.print(report["summary"])
    console.print()
    console.print(report["content"])


if __name__ == "__main__":
    main()