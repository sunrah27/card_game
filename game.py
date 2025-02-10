import pygame
from config import *
from card import WitchCard, EnemyCard
from stack import Stack
from ability import *
from render import Render

# Define game setup function
def setup_game():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Card Game")

    # Create instances of cards
    witch1 = WitchCard("Fire Witch", "A fiery sorceress.", "Hot-headed and fearless.", "witch.png", (237, 81, 185), -1, 4, 1,  "Witch", 1, 400, 400, witch_abilities)
    witch2 = WitchCard("Ninja", "A sneaky ninja.", "Quiet and stealthy, hides in the shadows.", "ninja.png", (237, 81, 185), -1, 2, 2, "Witch", 1, 50, 50, witch_abilities)
    witch3 = WitchCard("Worker", "A hard worker.", "A busy body always building something.", "boy.png", (237, 81, 185), -1, 1, 4, "Witch", 1, 50, 50, witch_abilities)

    enemy = EnemyCard("Zombie", "A sneaky zombie.", "Smelly and green.", "zombine.png", (216, 57, 71), -1, 2, 1, "Enemy", 1, 210, 50, enemy_abilities)

    # Create stack
    game_manager = [
        Stack(100, 100, [witch1, witch2, witch3]),
        Stack(300, 100, [enemy]),
        Stack(500, 100, [witch1, witch2, witch3]),
    ]

    return screen, game_manager, Render(screen)

def game_loop(screen, game_manager, render):
    clock = pygame.time.Clock()
    dragging_stack = None
    drag_offset = (0, 0)
    SNAP_DISTANCE = 50

    while True:
        screen.fill(BG_COLOUR)  # Clear screen with a background color
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
            # Handle mouse input
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for stack in reversed(game_manager):
                    index = stack.get_clicked_card_index(mouse_pos)
                    if index != -1:
                        dragging_stack = stack.split(index)
                        if dragging_stack:
                            drag_offset = (mouse_pos[0] - dragging_stack.x, mouse_pos[1] - dragging_stack.y)
                            game_manager.append(dragging_stack)
                        break
            
            elif event.type == pygame.MOUSEMOTION and dragging_stack:
                mouse_pos = pygame.mouse.get_pos()
                dragging_stack.update_position(mouse_pos, drag_offset)

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and dragging_stack:
                closest_stack = None
                min_distance = float('inf')

                # Find closest stack to snap to
                for stack in game_manager:
                    if stack == dragging_stack or not stack.cards:
                        continue
                    dx = dragging_stack.x - stack.x
                    dy = dragging_stack.y - (stack.y + len(stack.cards)*30)
                    distance = (dx**2 + dy**2)**0.5
                    if distance < SNAP_DISTANCE and distance < min_distance:
                        min_distance = distance
                        closest_stack = stack

                # Merge stacks or create new
                if closest_stack:
                    for card in dragging_stack.cards:
                        closest_stack.add_card(card)
                    game_manager.remove(dragging_stack)
                else:
                    # Boundary check
                    if not (0 < dragging_stack.x < SCREEN_WIDTH-150 and 
                           0 < dragging_stack.y < SCREEN_HEIGHT-210):
                        # Return to original stack
                        pass

                dragging_stack = None

        # Clean up empty stacks
        game_manager[:] = [stack for stack in game_manager if stack.cards]

        # Render all stacks
        for stack in game_manager:
            render.draw_stack(stack)

        pygame.display.flip()
        clock.tick(FPS)  # Set FPS