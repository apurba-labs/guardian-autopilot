import typer

from src.cli.commands.version import app as version_app
from src.cli.commands.doctor import app as doctor_app
from src.cli.commands.scan import app as scan_app
from src.cli.commands.serve import app as serve_app
from src.cli.commands.explain import app as explain_app

app = typer.Typer(
    name="guardian",
    help="🛡 Guardian Autopilot CLI",
    no_args_is_help=True,
)

app.add_typer(version_app)
app.add_typer(doctor_app)
app.add_typer(scan_app)
app.add_typer(serve_app)
app.add_typer(explain_app)

if __name__ == "__main__":
    app()