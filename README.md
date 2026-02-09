# 🎵 AutoSuno - Random Song Creator

Create random songs with a single click using Google Gemini AI and Suno AI!

## Overview

AutoSuno is an automated song creation tool that combines:
- **Google Gemini AI** - Generates creative song concepts, themes, and prompts
- **Producer Logic** - Orchestrates the workflow and optimizes prompts
- **Suno AI** - Creates the actual music (via https://suno.com/create)

Press one button and get a unique, AI-generated song concept ready to produce on Suno!

## Features

✨ **One-Click Creation** - Single button press to generate a complete song concept  
🎨 **Creative AI** - Uses Google Gemini to create unique themes and ideas  
🎵 **Genre Selection** - Choose from multiple genres or go random  
🌐 **Web Interface** - Beautiful web UI that can be added to your home screen  
💻 **CLI Support** - Command-line interface for quick generation  
📱 **PWA Ready** - Add to home screen on mobile devices  

## Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/ppatty/AutoSuno.git
cd AutoSuno

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Google Gemini API key
# Get your key from: https://makersuite.google.com/app/apikey
```

Edit `.env` file:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Run the Application

**Option A: Web Interface (Recommended)**

```bash
python web_app.py
```

Then open http://localhost:5000 in your browser. You can add this to your home screen for one-click access!

**Option B: Command Line**

```bash
# Create a random song
python autosuno.py

# Create a song in a specific genre
python autosuno.py --genre rock

# Create and save the result
python autosuno.py --save
```

## How It Works

1. **🎯 Generate Concept**: Google Gemini creates a unique song concept with title, theme, mood, and style
2. **✨ Optimize Prompt**: The Producer enhances the concept into a Suno-optimized prompt
3. **🎵 Ready for Suno**: Get your prompt ready to paste into Suno AI at https://suno.com/create

## Usage Examples

### Web Interface

1. Open http://localhost:5000
2. (Optional) Select a genre or leave it random
3. Click the big music icon 🎸
4. Wait for the AI to generate your song concept
5. Copy the Suno prompt and click "Open Suno AI" to create your song!

### Command Line

```bash
# Random song
python autosuno.py

# Rock song
python autosuno.py --genre rock

# Jazz song and save to file
python autosuno.py --genre jazz --save --output my_jazz_song.json
```

## Available Genres

- Pop
- Rock
- Jazz
- Electronic
- Hip-Hop
- Classical

You can customize the genre list in `.env`:
```
SONG_GENRES=pop,rock,jazz,electronic,hip-hop,classical,country,blues
```

## Adding to Home Screen

### iOS (iPhone/iPad)
1. Open the web interface in Safari
2. Tap the Share button
3. Select "Add to Home Screen"
4. Tap "Add"

### Android
1. Open the web interface in Chrome
2. Tap the menu (three dots)
3. Select "Add to Home Screen"
4. Tap "Add"

Now you have a one-click song creator on your home screen!

## Project Structure

```
AutoSuno/
├── autosuno.py          # CLI entry point
├── web_app.py           # Web interface (Flask)
├── config.py            # Configuration management
├── gemini_generator.py  # Google Gemini integration
├── suno_client.py       # Suno AI client
├── producer.py          # Main orchestration logic
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
├── templates/           # Web templates
│   └── index.html      # Main web interface
└── static/             # Static assets
    └── manifest.json   # PWA manifest
```

## API Keys

### Google Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key to your `.env` file

### Suno API (Optional)
Currently, Suno doesn't have a public API. The application generates optimized prompts that you can use manually on https://suno.com/create. If Suno releases an official API in the future, you can add your credentials to the `.env` file.

## Troubleshooting

**Issue**: "GEMINI_API_KEY is required"
- **Solution**: Make sure you copied `.env.example` to `.env` and added your API key

**Issue**: Web interface doesn't load
- **Solution**: Ensure Flask is installed (`pip install flask`) and port 5000 is available

**Issue**: Import errors
- **Solution**: Install all dependencies with `pip install -r requirements.txt`

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## License

MIT License - feel free to use this for your own projects!

## Acknowledgments

- Google Gemini AI for creative content generation
- Suno AI for music creation
- The open-source community

---

Made with ❤️ and 🤖 AI
