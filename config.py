"""
Configuration management for AutoSuno
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Application configuration"""
    
    # API Keys
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
    SUNO_API_KEY = os.getenv('SUNO_API_KEY', '')
    
    # Song settings
    SONG_GENRES = os.getenv('SONG_GENRES', 'pop,rock,jazz,electronic,hip-hop,classical').split(',')
    
    # Suno settings
    SUNO_BASE_URL = 'https://suno.com/api'  # Note: This may need to be updated based on actual API
    
    @classmethod
    def validate(cls):
        """Validate required configuration"""
        if not cls.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is required. Please set it in .env file")
        
        return True
