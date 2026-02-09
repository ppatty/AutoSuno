"""
Web interface for AutoSuno - can be added to home screen
"""
from flask import Flask, render_template, jsonify, request
from config import Config
from producer import Producer
import os

app = Flask(__name__)
producer = Producer()


@app.route('/')
def index():
    """Main page with the create button"""
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create_song():
    """API endpoint to create a random song"""
    try:
        data = request.get_json() or {}
        genre = data.get('genre', None)
        
        # Create the song
        result = producer.create_random_song(genre=genre)
        
        return jsonify({
            'success': True,
            'result': result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/history')
def history():
    """Get creation history"""
    return jsonify({
        'history': producer.get_history()
    })


@app.route('/genres')
def genres():
    """Get available genres"""
    return jsonify({
        'genres': Config.SONG_GENRES
    })


if __name__ == '__main__':
    try:
        Config.validate()
        print("\n" + "="*60)
        print("🎵 AutoSuno Web Interface")
        print("="*60)
        print("\nStarting server at http://localhost:5000")
        print("Open this URL in your browser and add it to your home screen!")
        print("\nPress Ctrl+C to stop the server")
        print("="*60 + "\n")
        
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("\nPlease copy .env.example to .env and add your API keys:")
        print("  cp .env.example .env")
        print("  # Edit .env and add your GEMINI_API_KEY")
