# OmniCode: The Modular, Multi-Model AI Assistant

OmniCode is not just another AI code generator; it's a **comprehensive framework** designed for developers who value efficiency, privacy, and power. It represents a new paradigm in AI-assisted development, offering unparalleled flexibility and control.

## 🚀 Key Features

### 🏗️ Modular Architecture
OmniCode is built on a clean, modular foundation. Every feature, from generation to refactoring, is a self-contained module, making the system easy to extend, maintain, and customize.

### 🧠 Hybrid AI Engine
Why choose between speed and power when you can have both? OmniCode intelligently selects the best AI model for the task at hand:
- **Local Models (via Ollama):** For rapid, private, and offline code generation. Perfect for quick tasks and sensitive codebases.
- **Cloud Models (via OpenAI):** For complex, nuanced tasks that require the most powerful AI models available.

### 🧠 AST-Aware Refactoring
This is our game-changing feature. Unlike simple prompt-based tools, OmniCode understands the *structure* of your code. It parses Python code into an Abstract Syntax Tree (AST) and sends this structural context to the AI. This results in **more reliable, accurate, and context-aware refactoring** that respects the logic of your original code.

### 🌐 Universal Editor Integration
With its built-in LSP Server (planned feature), OmniCode is designed to integrate with any LSP-compatible editor (VS Code, Neovim, Vim, etc.), bringing its power directly into your favorite development environment.

## 🛠️ Quick Start

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Wanbogang/omnicode-assistant.git
    cd omnicode-assistant
    ```

2.  **Setup the environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -e .
    ```

3.  **Configure your environment:**
    *   Install [Ollama](https://ollama.com/) for local models.
    *   Copy `.env.example` to `.env` and add your OpenAI API key.
    *   `export PYTHONPATH="${PYTHONPATH}:/path/to/your/project"`

4.  **Run the commands:**
    ```bash
    # Generate code with a powerful cloud model
    omnicode generate "Create a Python function to fetch data from a URL"

    # Generate code with a fast, private local model
    omnicode generate "Create a Python function to fetch data from a URL" --local

    # Refactor code using AI's understanding of its structure
    omnicode refactor path/to/your/file.py
    ```

## 🏆 Why OmniCode is Different

The current landscape of AI code assistants is filled with simple wrappers for cloud APIs. OmniCode is different. It's a statement about the future of development tools:
-   **Privacy-First:** Your code stays on your machine.
-   **Hybrid by Design:** Get the speed of local models and the power of cloud models in one tool.
-   **Architecturally Sound:** Built for extensibility and long-term maintenance.
-   **Intelligent:** Understands your code's structure, not just its text.

## 📜 Philosophy

This project was built to win. It demonstrates a deep understanding of software architecture, AI/ML concepts, and the real-world needs of developers. It's not just a tool; it's a platform for the next generation of developers.
