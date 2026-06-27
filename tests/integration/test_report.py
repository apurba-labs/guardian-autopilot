from pathlib import Path
from uuid import uuid4

from rich.console import Console

from src.agents.decision_agent import DecisionAgent
from src.agents.investigation_agent import InvestigationAgent
from src.agents.parser_agent import ParserAgent
from src.agents.report_agent import ReportAgent
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
    decision = DecisionAgent(provider)
    report = ReportAgent()

    incident = parser.run(incident)
    incident = investigator.run(incident)
    incident = decision.run(incident)
    incident = report.run(incident)

    data = incident.metadata["report"]

    console.rule("[bold green]Guardian Incident Report")

    console.print(f"[bold]{data['title']}[/]")
    console.print()

    console.print(data["summary"])
    console.print()

    console.print(data["content"])


if __name__ == "__main__":
    main()