import subprocess
import json
from .config import Config

class ModelManager:
    def __init__(self):
        self.config = Config()

    def generate_code(self, prompt: str, language: str = "python", use_local: bool = False):
        if use_local:
            return self._generate_with_ollama(prompt, language)
        else:
            return "[yellow]Cloud model is temporarily disabled. Please use the --local flag to use the local Ollama model.[/yellow]"

    def _generate_with_ollama(self, prompt: str, language: str):
        full_prompt = f"Generate code in {language} for the following request. Only provide the code block, no explanations.\n\nRequest: {prompt}"
        
        payload_dict = {
            "model": "qwen:0.5b",
            "messages": [{"role": "user", "content": full_prompt}],
            "stream": False
        }
        
        json_payload = json.dumps(payload_dict)
        
        curl_command = [
            "curl", "http://localhost:11434/v1/chat/completions",
            "-H", "Content-Type: application/json",
            "-d", json_payload
        ]
        
        try:
            result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
            
            response_json = json.loads(result.stdout)
            if "choices" in response_json and len(response_json["choices"]) > 0:
                return response_json["choices"][0]["message"]["content"]
            else:
                return f"[red]Error: Could not parse response. Raw output: {result.stdout}[/red]"

        except subprocess.CalledProcessError as e:
            return f"[red]Error executing curl: {e.stderr}[/red]"
        except Exception as e:
            return f"[red]An error occurred: {e}[/red]"
