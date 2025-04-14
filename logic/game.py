import pygame
from logic.game_state import GameStateManager
from screens.start_screen import StartScreen
from screens.character_selection_screen import CharacterSelectionScreen
from screens.gameplay_screen import GameplayScreen
from config import *

# Initilise Pygame
pygame.display.set_caption("Card Game")

class Game:
    def __init__(self):
        pygame.init()

        # Set up screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Card Game")

        # Create game state manager
        self.game_state_manager = GameStateManager(self.screen)

        # Create screens
        self.start_screen = StartScreen(self.screen, self.game_state_manager)
        self.character_selection_screen = CharacterSelectionScreen(self.screen, self.game_state_manager)
        self.gameplay_screen = GameplayScreen(self.screen, self.game_state_manager)

        # Add screens to the game state manager
        self.game_state_manager.add_screen("start_screen", self.start_screen)
        self.game_state_manager.add_screen("character_selection_screen", self.character_selection_screen)
        self.game_state_manager.add_screen("gameplay_screen", self.gameplay_screen)

        # Set the initial state to the start screen
        self.game_state_manager.change_state("start_screen")


    def run(self):
        """Start the game."""
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.game_state_manager.handle_input()

            # Render the current screen
            self.game_state_manager.render()

            pygame.display.flip()
            clock.tick(FPS)