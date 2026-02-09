# Quick Start Guide

## Get Your AutoSuno Up and Running in 5 Minutes! 🚀

### Step 1: Get a Google Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your new API key

### Step 2: Set Up AutoSuno

```bash
# Clone the repo
git clone https://github.com/ppatty/AutoSuno.git
cd AutoSuno

# Install requirements
pip install -r requirements.txt

# Create your .env file
cp .env.example .env
```

### Step 3: Add Your API Key

Edit the `.env` file and replace `your_gemini_api_key_here` with your actual key:

```
GEMINI_API_KEY=AIzaSy...your_actual_key_here
```

### Step 4: Create Your First Song!

**Option 1: Web Interface (Recommended)**

```bash
python web_app.py
```

Open http://localhost:5000 and click the music icon! 🎸

**Option 2: Command Line**

```bash
python autosuno.py
```

### Step 5: Use on Suno

1. Copy the generated Suno prompt
2. Go to https://suno.com/create
3. Paste the prompt
4. Click Create!
5. Enjoy your AI-generated music! 🎵

## Add to Your Phone's Home Screen

### iPhone/iPad
1. Open http://localhost:5000 (or your server URL) in Safari
2. Tap the Share button (square with arrow)
3. Scroll and tap "Add to Home Screen"
4. Name it "AutoSuno" and tap "Add"

### Android
1. Open the site in Chrome
2. Tap the menu (⋮)
3. Tap "Add to Home Screen"
4. Name it "AutoSuno" and tap "Add"

Now you can create random songs with just one tap! 🎉

## Troubleshooting

**Problem**: Import errors
```bash
pip install -r requirements.txt
```

**Problem**: API key not working
- Make sure you copied the entire key
- Check there are no extra spaces
- Verify the key is active in Google AI Studio

**Problem**: Port 5000 already in use
```bash
# Use a different port
python -c "from web_app import app; app.run(port=8080)"
```

## What's Next?

- Try different genres (pop, rock, jazz, electronic, hip-hop, classical)
- Save your favorite prompts with `--save`
- Share your creations!

Happy music making! 🎶
