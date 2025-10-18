import click
from rich.console import Console
from ..utils.ast_parser import parse_file_to_ast, ast_to_code

console = Console()

@click.command()
@click.argument("file_path")
@click.option("--apply", is_flag=True, help="Apply the refactoring changes directly to the file.")
def refactor_command(file_path: str, apply: bool):
    """
    (Placeholder) Refactors code using AI.
    """
    console.print(f"[bold yellow]Refactoring file:[/bold yellow] {file_path}")
    
    ast_representation = parse_file_to_ast(file_path)
    console.print(f"[green]✅ Parsed to AST:[/green]\n{ast_representation}\n")
    
    console.print("[yellow]🤖 (Next step: Send AST to AI for refactoring)[/yellow]")
    
    if apply:
        console.print("Changes will be applied to the file.")
    else:
        console.print("Changes will be shown as a diff.")
