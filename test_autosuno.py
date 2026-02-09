"""
Unit tests for AutoSuno components
"""
import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import Config


class TestConfig(unittest.TestCase):
    """Test configuration module"""
    
    def test_config_has_required_attributes(self):
        """Test that Config has all required attributes"""
        self.assertTrue(hasattr(Config, 'GEMINI_API_KEY'))
        self.assertTrue(hasattr(Config, 'SUNO_API_KEY'))
        self.assertTrue(hasattr(Config, 'SONG_GENRES'))
        self.assertTrue(hasattr(Config, 'SUNO_BASE_URL'))
    
    def test_song_genres_is_list(self):
        """Test that SONG_GENRES is a list"""
        self.assertIsInstance(Config.SONG_GENRES, list)
        self.assertGreater(len(Config.SONG_GENRES), 0)
    
    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'})
    def test_validate_with_key(self):
        """Test validation with API key present"""
        # Reload config with patched environment
        import importlib
        import config
        importlib.reload(config)
        from config import Config as ReloadedConfig
        
        # Should not raise an exception
        try:
            ReloadedConfig.validate()
        except ValueError:
            self.fail("validate() raised ValueError unexpectedly")
    
    def test_validate_without_key_raises_error(self):
        """Test validation without API key raises error"""
        # Save original key
        original_key = Config.GEMINI_API_KEY
        
        # Temporarily remove key
        Config.GEMINI_API_KEY = ''
        
        # Should raise ValueError
        with self.assertRaises(ValueError):
            Config.validate()
        
        # Restore original key
        Config.GEMINI_API_KEY = original_key


class TestGeminiGenerator(unittest.TestCase):
    """Test Gemini generator module"""
    
    @patch('gemini_generator.genai')
    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'})
    def test_gemini_generator_init(self, mock_genai):
        """Test GeminiGenerator initialization"""
        from gemini_generator import GeminiSongGenerator
        
        generator = GeminiSongGenerator()
        
        # Verify genai was configured
        mock_genai.configure.assert_called_once()
    
    @patch('gemini_generator.genai')
    @patch.dict(os.environ, {'GEMINI_API_KEY': 'test_key'})
    def test_generate_song_prompt_structure(self, mock_genai):
        """Test that generate_song_prompt returns correct structure"""
        from gemini_generator import GeminiSongGenerator
        
        # Mock the response
        mock_response = Mock()
        mock_response.text = """Title: Test Song
        This is a test song about testing.
        Mood: Happy
        Style: Upbeat"""
        
        mock_model = Mock()
        mock_model.generate_content.return_value = mock_response
        mock_genai.GenerativeModel.return_value = mock_model
        
        generator = GeminiSongGenerator()
        result = generator.generate_song_prompt('pop')
        
        # Verify structure
        self.assertIn('title', result)
        self.assertIn('genre', result)
        self.assertIn('description', result)
        self.assertIn('full_prompt', result)
        self.assertEqual(result['genre'], 'pop')


class TestSunoClient(unittest.TestCase):
    """Test Suno client module"""
    
    def test_suno_client_init(self):
        """Test SunoClient initialization"""
        from suno_client import SunoClient
        
        client = SunoClient()
        self.assertIsNotNone(client.base_url)
        self.assertIsNotNone(client.session)
    
    def test_create_song_returns_structure(self):
        """Test that create_song returns correct structure"""
        from suno_client import SunoClient
        
        client = SunoClient()
        result = client.create_song(
            prompt="Test prompt",
            title="Test Song",
            genre="pop"
        )
        
        # Verify structure
        self.assertIn('title', result)
        self.assertIn('genre', result)
        self.assertIn('prompt', result)
        self.assertIn('status', result)
        self.assertIn('instructions', result)


class TestProducer(unittest.TestCase):
    """Test Producer module"""
    
    @patch('producer.GeminiSongGenerator')
    @patch('producer.SunoClient')
    def test_producer_init(self, mock_suno, mock_gemini):
        """Test Producer initialization"""
        from producer import Producer
        
        producer = Producer()
        
        # Verify components were initialized
        mock_gemini.assert_called_once()
        mock_suno.assert_called_once()
        self.assertEqual(len(producer.history), 0)
    
    @patch('producer.GeminiSongGenerator')
    @patch('producer.SunoClient')
    def test_create_random_song_workflow(self, mock_suno_class, mock_gemini_class):
        """Test the complete song creation workflow"""
        from producer import Producer
        
        # Mock Gemini
        mock_gemini = Mock()
        mock_gemini.generate_song_prompt.return_value = {
            'title': 'Test Song',
            'genre': 'pop',
            'description': 'Test description',
            'full_prompt': 'Test prompt'
        }
        mock_gemini.enhance_prompt_for_suno.return_value = 'Enhanced prompt'
        mock_gemini_class.return_value = mock_gemini
        
        # Mock Suno
        mock_suno = Mock()
        mock_suno.create_song.return_value = {
            'status': 'ready_to_create',
            'instructions': 'Test instructions'
        }
        mock_suno_class.return_value = mock_suno
        
        # Create producer and song
        producer = Producer()
        result = producer.create_random_song('pop')
        
        # Verify workflow was called
        mock_gemini.generate_song_prompt.assert_called_once()
        mock_gemini.enhance_prompt_for_suno.assert_called_once()
        mock_suno.create_song.assert_called_once()
        
        # Verify result structure
        self.assertIn('timestamp', result)
        self.assertIn('song_concept', result)
        self.assertIn('suno_prompt', result)
        self.assertIn('suno_result', result)
        self.assertIn('status', result)
        
        # Verify history was updated
        self.assertEqual(len(producer.history), 1)


if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)
