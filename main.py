import pygame
from game import setup_game, game_loop

pygame.init()

# Main entry point of the script
if __name__ == "__main__":
    screen, game_manager, button, render = setup_game()
    game_loop(screen, game_manager,button, render)

    # Quit Pygame
    pygame.quit()