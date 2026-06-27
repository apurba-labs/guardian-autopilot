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
    console.print(incident.model_dump())


if __name__ == "__main__":
    main()