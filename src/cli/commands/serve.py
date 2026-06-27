import uvicorn
import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def serve(
    host: str = "0.0.0.0",
    port: int = 8000,
):
    """Start Guardian Autopilot REST API."""

    console.print(
        f"🚀 Starting Guardian Autopilot API on http://{host}:{port}"
    )

    uvicorn.run(
        "src.api.app:app",
        host=host,
        port=port,
        reload=True,
    )