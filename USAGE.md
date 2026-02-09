# AutoSuno Usage Guide

## Complete Guide to Using AutoSuno

### What AutoSuno Does

AutoSuno automates the creative process of song generation by:
1. Using Google Gemini AI to create unique song concepts
2. Optimizing those concepts into perfect prompts for Suno AI
3. Providing you with everything you need to create music on Suno

### Installation & Setup

See [QUICKSTART.md](QUICKSTART.md) for detailed setup instructions.

Quick version:
```bash
git clone https://github.com/ppatty/AutoSuno.git
cd AutoSuno
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### Usage Methods

#### 1. Web Interface (Best for Mobile/Home Screen)

**Start the server:**
```bash
python web_app.py
```

**Access:**
- Open http://localhost:5000 in your browser
- Click the big music icon to create a song
- Optionally select a genre before clicking

**Add to Home Screen:**
- **iOS**: Safari → Share → Add to Home Screen
- **Android**: Chrome → Menu → Add to Home Screen

Now you have a one-tap song creator!

#### 2. Command Line Interface

**Basic usage:**
```bash
python autosuno.py
```

**With options:**
```bash
# Specific genre
python autosuno.py --genre rock

# Save output to file
python autosuno.py --save

# Custom output filename
python autosuno.py --genre jazz --save --output my_jazz_song.json
```

**Help:**
```bash
python autosuno.py --help
```

#### 3. Python API

Use AutoSuno in your own Python scripts:

```python
from producer import Producer

# Create a producer
producer = Producer()

# Generate a random song
result = producer.create_random_song()

# Generate a specific genre
rock_song = producer.create_random_song(genre='rock')

# Save the result
producer.save_result(result, 'my_song.json')

# Access the data
print(f"Title: {result['song_concept']['title']}")
print(f"Suno Prompt: {result['suno_prompt']}")
```

### Available Genres

Default genres:
- `pop`
- `rock`
- `jazz`
- `electronic`
- `hip-hop`
- `classical`

**Customize genres** by editing `.env`:
```env
SONG_GENRES=pop,rock,jazz,electronic,hip-hop,classical,country,blues,reggae
```

### Output Format

AutoSuno generates:

1. **Song Concept** (from Gemini)
   - Title
   - Theme/Story
   - Mood
   - Style suggestions
   - Sample lyrics/hooks

2. **Suno Prompt** (optimized)
   - Concise description
   - Musical elements
   - Mood and instrumentation
   - Ready to paste into Suno

### Using with Suno

1. **Generate your song concept** with AutoSuno
2. **Copy the "Suno Prompt"** from the output
3. **Go to** https://suno.com/create
4. **Paste the prompt** into Suno
5. **Add the title** (optional but recommended)
6. **Click "Create"** and wait for your music!

### Examples

#### Example 1: Quick Random Song
```bash
$ python autosuno.py
```
Creates a random song in a random genre.

#### Example 2: Web Interface
```bash
$ python web_app.py
# Open http://localhost:5000
# Click 🎸 button
```

#### Example 3: Multiple Songs
```python
from producer import Producer

producer = Producer()

# Create 5 different songs
for _ in range(5):
    song = producer.create_random_song()
    producer.save_result(song)

# View history
print(f"Created {len(producer.get_history())} songs")
```

#### Example 4: Genre-Specific Batch
```bash
# Create 3 rock songs
for i in {1..3}; do
  python autosuno.py --genre rock --save --output "rock_song_$i.json"
done
```

### Tips & Tricks

1. **Genre Selection**: 
   - Leave genre empty for creative surprises
   - Specify genre for consistent style

2. **Prompt Editing**:
   - Feel free to edit the Suno prompt before using it
   - Add specific instruments or remove elements

3. **Batch Creation**:
   - Use the web interface for one-off creations
   - Use CLI with scripts for batch generation

4. **Mobile Usage**:
   - Add to home screen for instant access
   - Works great on tablets too

5. **Save Your Favorites**:
   - Use `--save` to keep track of great prompts
   - JSON files are easy to search and organize

### Troubleshooting

**"GEMINI_API_KEY is required"**
- Make sure you created `.env` from `.env.example`
- Add your actual API key to `.env`

**Web interface won't start**
- Check if port 5000 is available
- Try a different port: edit `web_app.py` and change `port=5000`

**"Module not found" errors**
- Install dependencies: `pip install -r requirements.txt`

**API quota exceeded**
- Gemini has rate limits on free tier
- Wait a few minutes or upgrade your API plan

### Advanced Usage

#### Custom Producer Logic

```python
from producer import Producer
from gemini_generator import GeminiSongGenerator

# Create custom producer
class MyProducer(Producer):
    def create_song_with_theme(self, theme):
        # Custom implementation
        pass

producer = MyProducer()
```

#### Integration with Other Tools

```python
from producer import Producer
import json

producer = Producer()

# Create song
result = producer.create_random_song()

# Send to your own API
import requests
requests.post('https://myapi.com/songs', 
              json=result['suno_prompt'])
```

### Demo Mode

Try the demo without an API key:

```bash
python demo.py
```

This shows you exactly what AutoSuno generates!

### File Structure

```
AutoSuno/
├── autosuno.py          # CLI interface
├── web_app.py           # Web interface
├── producer.py          # Main orchestrator
├── gemini_generator.py  # Gemini AI integration
├── suno_client.py       # Suno placeholder/guide
├── config.py            # Configuration
├── demo.py              # Demo without API key
├── example.py           # Example usage
└── test_autosuno.py     # Unit tests
```

### Contributing

Want to improve AutoSuno? Contributions welcome!

- Add new features
- Improve prompts
- Add genre templates
- Enhance the UI

### Getting Help

1. Check [README.md](README.md)
2. Check [QUICKSTART.md](QUICKSTART.md)
3. Run `python autosuno.py --help`
4. Check the issues on GitHub

---

Happy creating! 🎵
