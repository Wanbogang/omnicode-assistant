import subprocess
import json
from openai import OpenAI
from rich.console import Console
from .config import Config


class ModelManager:
    def __init__(self):
        self.config = Config()
        self.openai_client = OpenAI(api_key=self.config.OPENAI_API_KEY)
        self.console = Console()

    def generate_code(self, prompt: str, language: str = "python", use_local: bool = False):
        if use_local:
            return self._generate_with_ollama(prompt, language)
        else:
            return self._generate_with_openai(prompt, language)

    def _generate_with_ollama(self, prompt: str, language: str):
        full_prompt = f"Generate code in {language} for the following request. Only provide the code block, no explanations.\n\nRequest: {prompt}"
        payload_dict = {"model": "qwen:0.5b", "messages": [{"role": "user", "content": full_prompt}], "stream": False}
        json_payload = json.dumps(payload_dict)
        curl_command = ["curl", "http://localhost:11434/v1/chat/completions", "-H", "Content-Type: application/json", "-d", json_payload]
        try:
            result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
            response_json = json.loads(result.stdout)
            return response_json["choices"][0]["message"]["content"]
        except subprocess.CalledProcessError as e:
            return f"[red]Error executing curl: {e.stderr}[/red]"
        except Exception as e:
            return f"[red]An error occurred: {e}[/red]"
            return f"[red]An error occurred: {e}[/red]"

    def _generate_with_openai(self, prompt: str, language: str):
        try:
            response = self.openai_client.chat.completions.create(
                model=self.config.CLOUD_MODEL_SIMPLE,
                messages=[
                    {"role": "system", "content": f"You are a helpful assistant that generates code in {language}. Only provide the code block, no explanations."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"An error occurred with OpenAI: {e}"

    def refactor_code_with_ast(self, ast_json_string: str, use_local: bool = False):
        """
        Sending AST representation to AI for refactoring.
        Secara default akan menggunakan model cloud yang paling kuat.
        """
        prompt = f"""
You are an expert Python developer. Your task is to refactor Python code based on a simplified JSON representation of its Abstract Syntax Tree (AST).

Your goal is to:
1.  Add type hints to all function arguments and return values.
2.  Add a clear and concise docstring to each function explaining what it does.
3.  Ensure the code is syntactically correct and follows PEP 8 guidelines.

Here is the input JSON:
```json
{ast_json_string}
```

Based on the JSON above, provide the complete, refactored Python code. Do not include any explanations, apologies, or text outside the code block. The output must be a single, valid Python code block.
"""
        
        if use_local:
            self.console.print("[yellow]Warning: Using local model for a complex task. Results may be suboptimal.[/yellow]")
            return self._generate_with_ollama(prompt, "python")
        else:
            self.console.print("[green]Using the most powerful cloud model for best results.[/green]")
            try:
                response = self.openai_client.chat.completions.create(
                    model=self.config.CLOUD_MODEL_COMPLEX, # Using gpt-4o
                    messages=[
                        {"role": "system", "content": "You are an expert Python assistant that outputs only valid code."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.2, # Slightly lower for more deterministic results
                )
                return response.choices[0].message.content
            except Exception as e:
                return f"An error occurred with OpenAI: {e}"
