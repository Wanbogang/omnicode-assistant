# OmniCode: Advanced AI-Powered Code Assistant

OmniCode is a modular, multi-model AI assistant designed for developers who value efficiency, privacy, and power.

## Key Features

-   **Modular Architecture:** Extensible commands for generation, refactoring, and translation.
-   **Hybrid AI Engine:** Seamlessly switches between fast, local models (Ollama) and powerful cloud models (OpenAI, Anthropic) to optimize for speed, cost, and quality.
-   **AST-Aware Refactoring:** Performs structurally-aware code refactoring for more reliable and accurate results.
-   **Universal Editor Integration:** Features a built-in LSP server for integration with any LSP-compatible editor (VS Code, Neovim, etc.).

## Installation

```bash
pip install .
Quick Start
Copy .env.example to .env and fill in your API keys.
Make sure you have Ollama installed and running for local models.
Run a command:
# Generate a function using a local model
omnicode generate "Create a python function to fetch data from a URL" --local

# Refactor a file using a powerful cloud model with AST analysis
omnicode refactor path/to/my/file.py --apply

# Start the LSP server for editor integration
omnicode lsp --stdio
Philosophy
This project is built to be different. Instead of a single-trick tool, OmniCode is a comprehensive framework that adapts to your workflow, prioritizing both cutting-edge capability and developer privacy.
