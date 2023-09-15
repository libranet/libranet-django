"""libranet_django.cli.

Command-line interface.
"""
from libranet_django import __version__

import typer

app = typer.Typer()

@app.callback()
def version_callback(value: bool):
    if value:
        typer.echo(f"{__version__}")
        raise typer.Exit()


@app.command()
def main() -> None:
    """libranet_django."""
    typer.echo("Hello libranet_django.")