import click
from rich.console import Console
from rich.syntax import Syntax
from ..core.model_manager import ModelManager

console = Console()

@click.command()
@click.argument("prompt")
@click.option("--local", is_flag=True, default=True, help="Use a local model via Ollama (default).")
@click.option("--language", default="python", help="Target programming language.")
def generate_command(prompt: str, local: bool, language: str):
    """
    Generates code from a natural language prompt.
    """
    console.print(f"[bold cyan]Generating code for:[/bold cyan] '{prompt}'")
    
    if local:
        console.print("[green]Using local model (Ollama with qwen:0.5b)...[/green]")
    else:
        console.print("[yellow]Cloud model is disabled for now.[/yellow]")
        return
        
    manager = ModelManager()
    response = manager.generate_code(prompt, language, use_local=True)
    
    if response.startswith("[red]"):
        console.print(response)
    else:
        syntax = Syntax(response, language, theme="monokai", line_numbers=True)
        console.print("\n--- Generated Code ---\n")
        console.print(syntax)
