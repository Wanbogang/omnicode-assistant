import click
from rich.console import Console

from .commands.generate import generate_command
from .commands.refactor import refactor_command

console = Console()

@click.group()
@click.version_option(version="0.1.0", prog_name="omnicode")
def cli():
    """
    OmniCode: Your modular, multi-model AI coding assistant.
    """
    pass

cli.add_command(generate_command, name="generate")
cli.add_command(refactor_command, name="refactor")

if __name__ == "__main__":
    cli()
