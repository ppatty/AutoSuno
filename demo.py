"""
Demo script - Shows AutoSuno functionality without requiring API keys
This demonstrates the workflow and output format
"""

from unittest.mock import Mock, patch
import sys


def demo_autosuno():
    """Demonstrate AutoSuno without requiring actual API keys"""
    
    print("\n" + "="*70)
    print("🎵 AutoSuno Demo - Random Song Creator")
    print("="*70 + "\n")
    
    # Mock the API responses
    with patch('gemini_generator.genai') as mock_genai:
        # Set up mock responses
        mock_model = Mock()
        
        # First call - generate concept
        concept_response = Mock()
        concept_response.text = """Title: "Electric Dreams in Neon"

A vibrant electronic pop song about the excitement and energy of city nightlife. 
This track captures the pulsing rhythm of urban life after dark.

Mood: Energetic, uplifting, modern
Style: Electronic pop with synthesizer leads, driving bassline, and crisp percussion

Sample lyrics/hook:
"Running through the city lights
Electric dreams in neon nights
Feel the rhythm, feel the beat
Dancing shadows on the street"

The song should have a bright, futuristic sound with layered synths and a memorable chorus."""
        
        # Second call - enhance for Suno
        enhanced_response = Mock()
        enhanced_response.text = """Create an upbeat electronic pop track with pulsing synthesizers and a driving four-on-the-floor beat. Features bright, futuristic synth leads layered over a deep bassline, crisp percussion, and atmospheric pads. The mood is energetic and uplifting, evoking the vibrant energy of city nightlife with neon-lit soundscapes and an infectious, danceable rhythm."""
        
        mock_model.generate_content.side_effect = [concept_response, enhanced_response]
        mock_genai.GenerativeModel.return_value = mock_model
        mock_genai.configure = Mock()
        
        # Mock the config to not require API key
        with patch.dict('os.environ', {'GEMINI_API_KEY': 'demo_key'}):
            from producer import Producer
            
            # Create and run
            producer = Producer()
            
            print("Creating a random Electronic song...\n")
            result = producer.create_random_song(genre='electronic')
            
            print("\n" + "="*70)
            print("📋 Demo Complete!")
            print("="*70)
            print("\nThis is what AutoSuno generates for you:")
            print(f"\n1. Song Title: {result['song_concept']['title']}")
            print(f"2. Genre: {result['song_concept']['genre']}")
            print(f"\n3. Full Creative Concept:")
            print(result['song_concept']['description'])
            print(f"\n4. Optimized Suno Prompt:")
            print(result['suno_prompt'])
            print("\n" + "="*70)
            print("\n✅ In real usage, you would:")
            print("   1. Copy the Suno prompt above")
            print("   2. Go to https://suno.com/create")
            print("   3. Paste the prompt")
            print("   4. Click 'Create' to generate your song!")
            print("\n" + "="*70 + "\n")


if __name__ == '__main__':
    try:
        demo_autosuno()
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
