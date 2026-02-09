"""
Example: Create a random song using AutoSuno
"""

# First, make sure you have set up your .env file with GEMINI_API_KEY

from producer import Producer

# Create a producer instance
producer = Producer()

# Example 1: Create a completely random song
print("Example 1: Random Song")
print("-" * 60)
result = producer.create_random_song()

# Example 2: Create a specific genre song
print("\n\nExample 2: Rock Song")
print("-" * 60)
rock_song = producer.create_random_song(genre='rock')

# Example 3: Save the result
print("\n\nExample 3: Create and Save")
print("-" * 60)
jazz_song = producer.create_random_song(genre='jazz')
producer.save_result(jazz_song, 'my_jazz_song.json')

# Example 4: View history
print("\n\nExample 4: View Session History")
print("-" * 60)
history = producer.get_history()
print(f"Created {len(history)} songs in this session:")
for i, song in enumerate(history, 1):
    print(f"{i}. {song['song_concept']['title']} ({song['song_concept']['genre']})")

print("\n✓ All examples completed!")
print("\nYou can now use these prompts on https://suno.com/create")
