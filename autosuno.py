#!/usr/bin/env python3
"""
AutoSuno - Main application entry point
Creates random songs with one command!
"""
import sys
import argparse
from config import Config
from producer import Producer


def main():
    """Main entry point for CLI"""
    parser = argparse.ArgumentParser(
        description='AutoSuno - Create random songs with Google Gemini and Suno AI'
    )
    parser.add_argument(
        '--genre',
        type=str,
        help=f'Specify a genre (options: {", ".join(Config.SONG_GENRES)})',
        default=None
    )
    parser.add_argument(
        '--save',
        action='store_true',
        help='Save the result to a JSON file'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Output filename for saved result',
        default=None
    )
    
    args = parser.parse_args()
    
    # Validate configuration
    try:
        Config.validate()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("\nPlease copy .env.example to .env and add your API keys:")
        print("  cp .env.example .env")
        print("  # Edit .env and add your GEMINI_API_KEY")
        sys.exit(1)
    
    # Create the producer and make a song!
    try:
        producer = Producer()
        result = producer.create_random_song(genre=args.genre)
        
        # Save if requested
        if args.save:
            producer.save_result(result, args.output)
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
