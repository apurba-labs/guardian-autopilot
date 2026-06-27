import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def version():
    """Show Guardian Autopilot version."""

    console.print("[bold blue]🛡 Guardian Autopilot[/]")
    console.print("Version : 1.0.0")
    console.print("Provider: Mock / Qwen Cloud")