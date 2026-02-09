"""
Producer - orchestrates the song creation workflow
"""
import json
from datetime import datetime
from gemini_generator import GeminiSongGenerator
from suno_client import SunoClient


class Producer:
    """
    The Producer orchestrates the entire song creation process:
    1. Generate creative concept with Gemini
    2. Optimize prompt for Suno
    3. Send to Suno for music generation
    """
    
    def __init__(self):
        """Initialize the producer with all necessary components"""
        self.gemini = GeminiSongGenerator()
        self.suno = SunoClient()
        self.history = []
    
    def create_random_song(self, genre=None):
        """
        Create a random song - the main workflow
        
        Args:
            genre: Optional genre specification
            
        Returns:
            dict: Complete song creation result
        """
        print("\n" + "="*60)
        print("🎵 AutoSuno Producer - Creating Your Random Song 🎵")
        print("="*60 + "\n")
        
        # Step 1: Generate song concept with Gemini
        print("Step 1: Generating creative song concept with Google Gemini...")
        song_concept = self.gemini.generate_song_prompt(genre)
        print(f"✓ Generated concept for: '{song_concept['title']}'")
        print(f"  Genre: {song_concept['genre']}")
        
        # Step 2: Enhance prompt for Suno
        print("\nStep 2: Optimizing prompt for Suno AI...")
        suno_prompt = self.gemini.enhance_prompt_for_suno(song_concept)
        print(f"✓ Prompt optimized")
        
        # Step 3: Send to Suno
        print("\nStep 3: Preparing song for Suno AI...")
        suno_result = self.suno.create_song(
            prompt=suno_prompt,
            title=song_concept['title'],
            genre=song_concept['genre']
        )
        
        # Compile final result
        result = {
            'timestamp': datetime.now().isoformat(),
            'song_concept': song_concept,
            'suno_prompt': suno_prompt,
            'suno_result': suno_result,
            'status': 'success'
        }
        
        # Save to history
        self.history.append(result)
        
        # Print summary
        self._print_summary(result)
        
        return result
    
    def _print_summary(self, result):
        """Print a nice summary of the creation process"""
        print("\n" + "="*60)
        print("🎉 Song Creation Complete! 🎉")
        print("="*60)
        print(f"\nTitle: {result['song_concept']['title']}")
        print(f"Genre: {result['song_concept']['genre']}")
        print(f"\nConcept:")
        print(result['song_concept']['description'])
        print(f"\nOptimized Suno Prompt:")
        print(result['suno_prompt'])
        print(f"\n{result['suno_result']['instructions']}")
        print("="*60 + "\n")
    
    def save_result(self, result, filename=None):
        """
        Save the result to a JSON file
        
        Args:
            result: The result dictionary to save
            filename: Optional filename, auto-generated if not provided
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"song_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(result, f, indent=2)
        
        print(f"✓ Result saved to: {filename}")
        return filename
    
    def get_history(self):
        """Get the history of all created songs in this session"""
        return self.history
