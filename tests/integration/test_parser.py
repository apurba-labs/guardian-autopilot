from pathlib import Path
from uuid import uuid4

from rich.console import Console
from src.services.ai.provider_factory import get_provider
from src.agents.parser_agent import ParserAgent
from src.core.qwen_client import QwenClient
from src.models.incident import Incident

console = Console()


def main() -> None:
    incident = Incident(
        id=str(uuid4()),
        source="fixture",
        raw_content=Path(
            "fixtures/incidents/leaked_credentials.txt"
        ).read_text(encoding="utf-8"),
    )

    provider = get_provider()
    parser = ParserAgent(provider)

    incident = parser.run(incident)

    console.rule("[bold green]Parser Agent Result")
    console.rule("[bold green]Parser Agent")

    console.print(f"[cyan]State:[/] {incident.state.value}")
    console.print(f"[cyan]Risk:[/] {incident.risk.value}")
    console.print()

    for finding in incident.findings:
        console.print(
            f"✓ {finding.type} "
            f"({finding.provider}) "
            f"[{finding.severity.value}] "
            f"{finding.confidence:.0%}"
        )


if __name__ == "__main__":
    main()