import pygame
import os
from ui.ui_manager import Button

class StartScreen:
    def __init__(self, screen, game_state_manager):
        self.screen = screen
        self.game_state_manager = game_state_manager

        # Load the background image using the correct path
        asset_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'bg_placeholder.png')
        self.background = pygame.image.load(asset_path)
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

        # Title text
        self.font = pygame.font.Font(None, 36)
        self.title_text = self.font.render("Start Screen", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(screen.get_width() // 2, 50))

        # Buttons
        self.new_game_button = Button("New Game", 100, 150, 200, 50, self.start_new_game)
        self.load_game_button = Button("Load Game", 100, 220, 200, 50, self.load_game)
        self.option_button = Button("Option", 100, 290, 200, 50, self.option)
        self.quit_button = Button("Quit", 100, 360, 200, 50, self.quit_game)

    def render(self):
        # Clear screen
        self.screen.blit(self.background, (0, 0))

        # Draw title
        self.screen.blit(self.title_text, self.title_rect)

        # Draw buttons
        self.new_game_button.render(self.screen)
        self.load_game_button.render(self.screen)
        self.option_button.render(self.screen)
        self.quit_button.render(self.screen)

    def handle_input(self):
        # Handle button clicks
        self.new_game_button.update()
        self.load_game_button.update()
        self.option_button.update()
        self.quit_button.update()

    def start_new_game(self):
        self.game_state_manager.change_state("character_selection_screen")

    def load_game(self):
        pass

    def option(self):
        pass

    def quit_game(self):
        pygame.quit()
        exit()