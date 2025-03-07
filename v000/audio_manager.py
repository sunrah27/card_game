# audio_manager.py - Manages sound effects and music
#     Loads and plays sound files.

class AudioManager:
    def __init__(self):
        self.sounds = {}  # Placeholder for storing sound files

    def load_sound(self, sound_name, sound_file):
        """Load a sound into the manager."""
        self.sounds[sound_name] = sound_file
        print(f"Sound {sound_name} loaded.")

    def play_sound(self, sound_name):
        """Play a sound."""
        if sound_name in self.sounds:
            print(f"Playing sound: {sound_name}")
        else:
            print(f"Sound {sound_name} not found.")
