import pygame
import os
from ui.ui_manager import Button

class CharacterSelectionScreen:
    def __init__(self, screen, game_state_manager):
        self.screen = screen
        self.game_state_manager = game_state_manager

        # Load the background image using the correct path
        asset_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_placeholder.png')
        self.background = pygame.image.load(asset_path)
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

        # Title text
        self.font = pygame.font.Font(None, 36)
        self.title_text = self.font.render("Character Selection", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(screen.get_width() // 2, 50))

        # Buttons
        self.witch_1_button = Button("Witch 1", 100, screen.get_height() // 2 - 50, 200, 50, self.select_witch_1)
        self.witch_2_button = Button("Witch 2", screen.get_width() - 300, screen.get_height() // 2 - 50, 200, 50, self.select_witch_2)
        self.back_button = Button("Back", 20, screen.get_height() - 50, 100, 40, self.go_back)

    def render(self):
        # Clear screen
        self.screen.blit(self.background, (0, 0))

        # Draw title
        self.screen.blit(self.title_text, self.title_rect)

        # Draw buttons
        self.witch_1_button.render(self.screen)
        self.witch_2_button.render(self.screen)
        self.back_button.render(self.screen)

    def handle_input(self):
        # Handle button clicks
        self.witch_1_button.update()
        self.witch_2_button.update()
        self.back_button.update()

    def select_witch_1(self):
        print("Witch 1 selected")
        # Add functionality for starting the game with Witch 1

    def select_witch_2(self):
        print("Witch 2 selected")
        # Add functionality for starting the game with Witch 2

    def go_back(self):
        # Go back to the start screen
        self.game_state_manager.change_state("start_screen")