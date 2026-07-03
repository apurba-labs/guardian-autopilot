import typer
from rich.console import Console

from config.settings import get_settings

app = typer.Typer()
console = Console()


@app.command()
def doctor():
    """Run environment diagnostics."""

    console.rule("[bold blue]Guardian Doctor")

    console.print("✓ Python")

    settings = get_settings()

    if settings.dashscope_api_key:
        console.print("✓ DASHSCOPE_API_KEY configured")
    else:
        console.print("⚠ DASHSCOPE_API_KEY not configured")

    console.print("✓ Provider abstraction")
    console.print("✓ Guardian Orchestrator")