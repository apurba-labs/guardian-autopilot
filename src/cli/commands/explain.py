from pathlib import Path
from uuid import uuid4

import typer
from rich.console import Console
from src.core.orchestrator import GuardianOrchestrator
from src.models.incident import Incident
from src.services.ai.provider_factory import get_provider

app = typer.Typer()
console = Console()

@app.command()
def explain(path: str):
    """Explain how Guardian Autopilot reached its decision."""

    incident = Incident(
        id=str(uuid4()),
        source="cli",
        raw_content=Path(path).read_text(encoding="utf-8"),
    )

    workflow = GuardianOrchestrator(get_provider())

    incident = workflow.run(incident)

    console.rule("[bold cyan]Guardian Autopilot - Explain")

    console.print(
        "[dim]Parser → Investigation → Decision → Report[/]"
    )

    console.print()

    console.print("[bold blue]Parser Agent[/]")

    for finding in incident.findings:
        console.print(
            f"✓ {finding.type} ({finding.provider}) "
            f"[{finding.severity.value}] "
            f"{finding.confidence:.0%}"
        )

    console.print()

    console.print("[bold yellow]Investigation Agent[/]")
    console.print(f"Risk      : {incident.risk.value}")
    console.print(f"Reason    : {incident.reasoning}")

    console.print()

    console.print("[bold red]Decision Agent[/]")
    console.print(f"Decision  : {incident.decision.value}")
    console.print(f"Reason    : {incident.decision_reasoning}")

    console.print()

    console.print("[bold green]Report Agent[/]")
    console.print("✓ Executive incident report generated successfully.")
