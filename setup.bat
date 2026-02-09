@echo off
REM AutoSuno Setup Script for Windows
REM This script helps you set up AutoSuno quickly

echo ==================================================
echo 🎵 AutoSuno Setup Script (Windows)
echo ==================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.7 or higher.
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✓ Found Python
python --version

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip is not installed. Please install pip.
    pause
    exit /b 1
)

echo ✓ Found pip
echo.

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo ✓ Dependencies installed successfully
) else (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo.

REM Check if .env exists
if exist .env (
    echo ✓ .env file already exists
) else (
    echo Creating .env file from template...
    copy .env.example .env
    echo ✓ Created .env file
    echo.
    echo ⚠️  IMPORTANT: Edit .env and add your GEMINI_API_KEY
    echo.
    echo Get your API key from:
    echo https://makersuite.google.com/app/apikey
)

echo.
echo ==================================================
echo ✅ Setup Complete!
echo ==================================================
echo.
echo Next steps:
echo 1. Edit .env and add your GEMINI_API_KEY
echo 2. Run the application:
echo    - Web interface: python web_app.py
echo    - Command line: python autosuno.py
echo.
echo For more help, see README.md or QUICKSTART.md
echo.
pause
