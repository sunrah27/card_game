import pygame
import time
from card import WitchCard, EnemyCard
from ability import *
from render import Render

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
FPS = 60
DAY_DURATION = 180
game_time = time.time()
curernt_day = 1

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Card Game")

# Create card objects
witch = WitchCard("witch1", "Fire Witch", "A fiery sorceress.", "Hot-headed and fearless.", "fire_witch.png", (237, 81, 185), -1, 4, 1, "Witch", 1, 50, 50, witch_abilities)
enemy = EnemyCard("enemy1", "Goblin", "A sneaky goblin.", "Smelly and green.", "goblin.png", (216, 57, 71), -1, 2, 1, "Enemy", 1, 210, 50, enemy_abilities)

# Initialize Render
render = Render(screen)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Attack action (e.g., pressing the space bar to attack)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Execute attack ability
                attack_ability = witch.abilities[0]  # Assuming the first ability is the attack
                attack_ability.execute(witch, enemy)

    # Clear screen
    screen.fill((0, 200, 150))  # Not white background.

    # Draw the witch card
    render.draw_card(witch)  # Example of drawing a card
    render.draw_card(enemy)
    # Update the display
    pygame.display.update()

    # Maintain framerate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()