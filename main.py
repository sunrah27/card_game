import pygame
from card import WitchCard, EnemyCard
from stack import Stack
from ability import *
from render import Render
from config import *
from game import setup_game, game_loop

pygame.init()

# Main entry point of the script
if __name__ == "__main__":
    screen, game_manager, render = setup_game()
    game_loop(screen, game_manager, render)

    # Quit Pygame
    pygame.quit()