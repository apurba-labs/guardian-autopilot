import typer

app = typer.Typer()

@app.command()
def scan(path: str):
    ...

@app.command()
def serve():
    ...