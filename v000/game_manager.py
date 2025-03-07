# game_manager.py

from ui_manager import UIManager, Button
from input_manager import InputManager
from audio_manager import AudioManager
from game_state import GameStateManager

class GameManager:
    def __init__(self):
        self.ui_manager = UIManager()
        self.input_manager = InputManager()
        self.audio_manager = AudioManager()
        self.game_state_manager = GameStateManager()

        # Create buttons for the start screen
        self.create_start_screen_buttons()
    
    def create_start_screen_buttons(self):
        """Create buttons for the start screen."""
        new_game_button = Button("New Game", self.start_new_game)
        load_game_button = Button("Load Game", self.load_game)
        options_button = Button("Options", self.open_options)
        quit_button = Button("Quit", self.quit_game)

        # Add buttons to the UI manager
        self.ui_manager.add_ui_element(new_game_button)
        self.ui_manager.add_ui_element(load_game_button)
        self.ui_manager.add_ui_element(options_button)
        self.ui_manager.add_ui_element(quit_button)
    
    def start_new_game(self):
        """Start a new game and change to the Character Selection screen."""
        print("Starting new game...")
        self.game_state_manager.change_state("character_selection")
    
    def load_game(self):
        """Load a saved game."""
        print("Loading game...")
        # Logic for loading a saved game
    
    def show_options(self):
        """Show the options screen."""
        print("Options screen...")
        # Transition to Options screen (not implemented yet)
    
    def quit_game(self):
        """Quit the game."""
        print("Quitting game...")

    def update(self):
        """Update all managers."""
        print("Updating Game Manager...")
        self.ui_manager.update()     # Update UI

    def render(self):
        """Render all managers."""
        print("Rendering Game Manager...")
        self.ui_manager.render()  # Render UI

    def start(self):
        """Start the game loop."""
        while True:
            self.update()
            self.render()
            # Simulate break to prevent infinite loop
            break
