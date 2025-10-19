import click
from rich.console import Console
from rich.syntax import Syntax
from ..utils.ast_parser import parse_file_to_ast, pretty_print_ast, ast_to_json
from ..core.model_manager import ModelManager

console = Console()

@click.command()
@click.argument("file_path")
@click.option("--apply", is_flag=True, help="Apply the refactoring changes directly to the file.")
def refactor_command(file_path: str, apply: bool):
    """
    Refactors code using AI based on its AST structure.
    """
    console.print(f"[bold yellow]Refactoring file:[/bold yellow] {file_path}")
    
    # Step 1: Parse code to AST
    ast_object = parse_file_to_ast(file_path)
    
    if isinstance(ast_object, str): # If there is a parsing error
        console.print(ast_object)
        return

    # Step 2: Convert AST to JSON
    ast_json = ast_to_json(ast_object)
    
    console.print("[green]✅ Parsed code to AST. Sending to AI...[/green]")
    
    # Step 3: Send to AI for refactoring
    manager = ModelManager()
    refactored_code = manager.refactor_code_with_ast(ast_json)
    
    # Step 4: Display results
    console.print("\n--- Refactored Code ---\n")
    if refactored_code.startswith("[red]"):
        console.print(refactored_code)
    else:
        syntax = Syntax(refactored_code, "python", theme="monokai", line_numbers=True)
        console.print(syntax)

    if apply:
        console.print("\n[yellow]Feature to apply changes is not yet implemented.[/yellow]")
    else:
        console.print("\n[yellow]Use --apply flag to write changes to the file.[/yellow]")
