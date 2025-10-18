import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL_DEFAULT = os.getenv("OLLAMA_MODEL_DEFAULT", "llama3:instruct")
    OLLAMA_MODEL_CODE = os.getenv("OLLAMA_MODEL_CODE", "codellama:instruct")
    CLOUD_MODEL_COMPLEX = os.getenv("CLOUD_MODEL_COMPLEX", "gpt-4o")
    CLOUD_MODEL_SIMPLE = os.getenv("CLOUD_MODEL_SIMPLE", "gpt-3.5-turbo")
