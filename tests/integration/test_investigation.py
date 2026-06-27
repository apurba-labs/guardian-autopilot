from pathlib import Path
from uuid import uuid4

from rich.console import Console

from src.agents.investigation_agent import InvestigationAgent
from src.agents.parser_agent import ParserAgent
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

    parser = ParserAgent(provider)
    investigator = InvestigationAgent(provider)

    incident = parser.run(incident)
    incident = investigator.run(incident)

    console.rule("[bold blue]Guardian Autopilot")

    console.print(
        f"[cyan]State:[/] {incident.state.value}"
    )

    console.print(
        f"[bold red]Risk:[/] {incident.risk.value}"
    )

    console.print()

    console.print("[bold]Reason[/]")
    console.print(incident.reasoning)

    console.print()

    console.print("[bold]Recommendations[/]")

    for item in incident.recommendation:
        console.print(f"✓ {item}")


if __name__ == "__main__":
    main()