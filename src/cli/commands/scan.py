import typer
from pathlib import Path
from uuid import uuid4



from rich.console import Console

from src.core.orchestrator import GuardianOrchestrator
from src.models.incident import Incident
from src.services.ai.provider_factory import get_provider

app = typer.Typer()
console = Console()

@app.command()
def scan(path: str):
    """Analyze an incident file and generate an executive report."""

    incident = Incident(
        id=str(uuid4()),
        source="cli",
        raw_content=Path(path).read_text(encoding="utf-8"),
    )

    workflow = GuardianOrchestrator(get_provider())

    incident = workflow.run(incident)

    report = incident.metadata["report"]

    console.rule("[bold blue]Guardian Autopilot")
    console.print(report["title"])
    console.print()
    console.print(report["summary"])
    console.print()
    console.print(report["content"])
