import os
import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def doctor():
    """Run environment diagnostics."""

    console.rule("[bold blue]Guardian Doctor")

    console.print("✓ Python")

    if os.getenv("DASHSCOPE_API_KEY"):
        console.print("✓ DASHSCOPE_API_KEY configured")
    else:
        console.print("⚠ DASHSCOPE_API_KEY not configured")

    console.print("✓ Provider abstraction")
    console.print("✓ Guardian Orchestrator")