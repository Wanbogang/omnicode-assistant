import ast
import json

def parse_file_to_ast(file_path: str):
    """Read Python file and return its AST representation."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code_string = f.read()
        return ast.parse(code_string)
    except FileNotFoundError:
        return f"[red]Error: File not found at {file_path}[/red]"
    except SyntaxError as e:
        return f"[red]Syntax Error in file: {e}[/red]"
    except Exception as e:
        return f"[red]Error reading file: {e}[/red]"

def _extract_function_info(node):
    """Extract information from a FunctionDef node."""
    info = {
        "type": "function",
        "name": node.name,
        "args": [arg.arg for arg in node.args.args],
        "body": []
    }
    for child in node.body:
        # Only take string representation of body node for simplicity
        info["body"].append(ast.unparse(child))
    return info

def ast_to_json(ast_object):
    """Convert AST to simple and structured JSON string."""
    if isinstance(ast_object, str):
        return json.dumps({"error": ast_object})
    
    summary = {"file_type": "python", "functions": []}
    
    for node in ast_object.body:
        if isinstance(node, ast.FunctionDef):
            summary["functions"].append(_extract_function_info(node))
            
    return json.dumps(summary, indent=2)

def pretty_print_ast(ast_object):
    """Print AST with neat formatting."""
    if isinstance(ast_object, str):
        return ast_object
    return ast_to_json(ast_object)
