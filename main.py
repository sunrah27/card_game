import pygame
from card import WitchCard, EnemyCard
from stack import Stack
from ability import *
from render import Render
from config import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Card Game")

witch1 = WitchCard("witch1", "Fire Witch", "A fiery sorceress.", "Hot-headed and fearless.", "witch.png", (237, 81, 185), -1, 4, 1, "Witch", 1, 50, 50, witch_abilities)

witch2 = WitchCard("witch1", "Ninja", "A sneaky ninja.", "Quiet and stealthy, hides in the shadows.", "ninja.png", (237, 81, 185), -1, 2, 2, "Witch", 1, 50, 50, witch_abilities)

witch3 = WitchCard("witch1", "Worker", "A hard worker.", "A busy body always building something.", "boy.png", (237, 81, 185), -1, 1, 4, "Witch", 1, 50, 50, witch_abilities)

enemy = EnemyCard("enemy1", "Zombie", "A sneaky zombie.", "Smelly and green.", "zombine.png", (216, 57, 71), -1, 2, 1, "Enemy", 1, 210, 50, enemy_abilities)

stack1 = Stack([witch1, witch2, witch3])
stack2 = Stack([enemy])
game_manager = [stack1, stack2]

def get_top_rect(mouse_pos, game_manager):
    for stack in reversed(game_manager):            # Check from the topmost stack to bottommost stack
        for card in reversed(stack.cards):          # Check from top card in the stack to the bottom card
            if card.rect.collidepoint(mouse_pos):
                return card                         # Return the card, not just the rect
    return None

render = Render(screen)

running = True
while running:
    screen.fill(BG_COLOUR)  # Not white background.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = event.pos
                selected_card = get_top_rect(mouse_pos, game_manager)
                if selected_card:
                    print(f"Selected Card: {selected_card.name}\npos: {selected_card.x},{selected_card.y}\n{selected_card.desc}\n{selected_card.flavour}")

    for item in game_manager:
        #print(f"Looping through game_manager, item type: {type(item)}")
        render.draw_stack(item)
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()