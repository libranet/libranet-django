"""
libranet_django.cli.

Command-line interface.
"""

import typer

from libranet_django import __version__

app = typer.Typer()


@app.callback()
def version_callback(*, value: bool = False) -> None:
    """Display the version of the application."""
    if value:
        typer.echo(f"{__version__}")
        raise typer.Exit


@app.command()
def main() -> None:
    """libranet_django."""
    typer.echo("Hello libranet_django.")
