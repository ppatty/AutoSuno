#!/bin/bash

# AutoSuno Setup Script
# This script helps you set up AutoSuno quickly

echo "=================================================="
echo "🎵 AutoSuno Setup Script"
echo "=================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null
then
    echo "❌ Python is not installed. Please install Python 3.7 or higher."
    exit 1
fi

# Determine Python command
if command -v python3 &> /dev/null
then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

echo "✓ Found Python: $PYTHON_CMD"

# Check if pip is installed
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null
then
    echo "❌ pip is not installed. Please install pip."
    exit 1
fi

# Determine pip command
if command -v pip3 &> /dev/null
then
    PIP_CMD="pip3"
else
    PIP_CMD="pip"
fi

echo "✓ Found pip: $PIP_CMD"
echo ""

# Install requirements
echo "Installing dependencies..."
$PIP_CMD install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""

# Check if .env exists
if [ -f .env ]; then
    echo "✓ .env file already exists"
else
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "✓ Created .env file"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your GEMINI_API_KEY"
    echo ""
    echo "Get your API key from:"
    echo "https://makersuite.google.com/app/apikey"
fi

echo ""
echo "=================================================="
echo "✅ Setup Complete!"
echo "=================================================="
echo ""
echo "Next steps:"
echo "1. Edit .env and add your GEMINI_API_KEY"
echo "2. Run the application:"
echo "   - Web interface: $PYTHON_CMD web_app.py"
echo "   - Command line: $PYTHON_CMD autosuno.py"
echo ""
echo "For more help, see README.md or QUICKSTART.md"
echo ""
