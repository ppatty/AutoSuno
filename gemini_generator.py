"""
Google Gemini integration for generating song prompts
"""
import google.generativeai as genai
from config import Config
import random


class GeminiSongGenerator:
    """Uses Google Gemini to generate creative song ideas"""
    
    def __init__(self):
        """Initialize Gemini API"""
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_song_prompt(self, genre=None):
        """
        Generate a random song prompt including theme, lyrics ideas, and mood
        
        Args:
            genre: Optional genre specification. If None, random genre is selected
            
        Returns:
            dict: Contains title, description, lyrics_style, and mood
        """
        if genre is None:
            genre = random.choice(Config.SONG_GENRES)
        
        prompt = f"""Create a unique and creative song concept for a {genre} song. 
        
Please provide:
1. A catchy song title
2. A brief description of what the song is about (theme/story)
3. The mood/emotion of the song
4. Style suggestions for the music
5. A few lines of sample lyrics or the main hook

Format your response as a clear, structured description."""

        try:
            response = self.model.generate_content(prompt)
            song_concept = response.text
            
            # Extract title from the response (simple parsing)
            lines = song_concept.split('\n')
            title = "Untitled Song"
            for line in lines:
                if 'title' in line.lower() and ':' in line:
                    title = line.split(':', 1)[1].strip()
                    # Remove quotes if present
                    title = title.strip('"').strip("'")
                    break
            
            return {
                'title': title,
                'genre': genre,
                'description': song_concept,
                'full_prompt': song_concept
            }
            
        except Exception as e:
            print(f"Error generating song prompt: {e}")
            # Return a fallback
            return {
                'title': f'Random {genre.capitalize()} Song',
                'genre': genre,
                'description': f'A creative {genre} song with unique vibes',
                'full_prompt': f'Create a {genre} song with a unique and creative sound'
            }
    
    def enhance_prompt_for_suno(self, song_concept):
        """
        Convert the Gemini-generated concept into a Suno-optimized prompt
        
        Args:
            song_concept: Dictionary containing the song concept
            
        Returns:
            str: Optimized prompt for Suno
        """
        enhancement_prompt = f"""Based on this song concept:

{song_concept['description']}

Create a concise, descriptive prompt (2-3 sentences) that would be perfect for an AI music generator. 
Focus on the mood, style, instrumentation, and key musical elements.
Keep it clear and specific."""

        try:
            response = self.model.generate_content(enhancement_prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Error enhancing prompt: {e}")
            return song_concept['description']
