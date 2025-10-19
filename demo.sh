#!/bin/bash

echo "=== OMNICODE DEMO ==="

echo "1. Generating code with a fast, private local model..."
echo "> Command: omnicode generate 'create a function that calculates the factorial of a number' --local"
echo ""
omnicode generate "create a function that calculates the number" --local

echo "========================================"

echo "2. Generating code with a powerful cloud model..."
echo "> Command: omnicode generate 'create a function that calculates the number'"
echo ""
omnicode generate "create a function that calculates the number"

echo "========================================"

echo "3. Refactoring code using AI's understanding of its structure (AST-aware refactoring)..."
echo "> Command: omnicode refactor sample_to_refactor.py"
echo ""
omnicode refactor sample_to_refactor.py

echo "========================================"
echo "Demo complete. Check out the repository for more details."
echo "https://github.com/Wanbogang/omnicode-assistant"
