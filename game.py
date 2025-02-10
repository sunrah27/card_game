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
    witch1 = WitchCard("witch1", "Fire Witch", "A fiery sorceress.", "Hot-headed and fearless.", "witch.png", (237, 81, 185), -1, 4, 1, "Witch", 1, 400, 400, witch_abilities)
    witch2 = WitchCard("witch1", "Ninja", "A sneaky ninja.", "Quiet and stealthy, hides in the shadows.", "ninja.png", (237, 81, 185), -1, 2, 2, "Witch", 1, 50, 50, witch_abilities)
    witch3 = WitchCard("witch1", "Worker", "A hard worker.", "A busy body always building something.", "boy.png", (237, 81, 185), -1, 1, 4, "Witch", 1, 50, 50, witch_abilities)

    enemy = EnemyCard("enemy1", "Zombie", "A sneaky zombie.", "Smelly and green.", "zombine.png", (216, 57, 71), -1, 2, 1, "Enemy", 1, 210, 50, enemy_abilities)

    # Create stack
    game_manager = [
        Stack(100, 100, [witch1, witch2, witch3]),
        Stack(250, 100, [enemy]),
    ]

    # Set up rendering
    render = Render(screen)

    return screen, game_manager, render


def game_loop(screen, game_manager, render):
    clock = pygame.time.Clock()
    running = True

    # Game loop function
    selected_stack = None           #selected stack
    selected_card = None            #selected card
    original_position = None        #original position of selected card
    original_mouse = None           #original mouse position
    new_stack = None                #new stack for dragging

    while running:
        screen.fill(BG_COLOUR)  # Clear screen with a background color
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            # Handle mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    selected_stack, selected_card = Render.get_top_rect(mouse_pos, game_manager)
                    if selected_stack and selected_card:

                        if original_mouse == None:
                            original_mouse = pygame.mouse.get_pos()
                            print(f"MD - {mouse_pos=}, {original_mouse=}")

                        if original_position == None:
                            original_position = (selected_card.x, selected_card.y)

                        if new_stack == None:
                            new_stack = Stack.remove_cards(selected_stack, selected_card)
                            print(f"MD - New stack:\n   -{new_stack}")

                        new_stack.x = mouse_pos[0] - 150 // 2
                        new_stack.y = mouse_pos[1] - 210 // 2
                        new_stack.cards[0].x = new_stack.x
                        new_stack.cards[0].y = new_stack.y

                        print(f"MD - Printing new_stack:\n   -{new_stack}")
                        print(f"MD - new_stack pos: {new_stack.x, new_stack.y=}")
                        print(f"MD - {mouse_pos=}, {original_mouse=}")
                        if new_stack and new_stack.cards:
                            game_manager.append(new_stack)
                            for i, stack in enumerate(game_manager):
                                for j, card in enumerate(stack.cards):
                                    print(f"MD - Stack:{i}, Card: {j} - {card.name}")
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    print(f"MU: {mouse_pos=}, {original_mouse=}, {original_position=}")
                    if mouse_pos == original_mouse:
                        print("MU - True")
                        selected_stack, selected_card = Render.get_top_rect(original_position, game_manager)

                        if selected_stack == None:
                            print("MU - Selected stack is None")
                            new_stack.x = original_position[0]
                            new_stack.y = original_position[1]
                            game_manager.append(Stack.add_card(new_stack, new_stack.cards[0]))
                        #print(f"MU - Selected stack:\n   -{selected_stack}, Selected card: {selected_card}")
                        
                        # if selected_stack is not None and new_stack is not None:
                        #     # Add the cards back to the selected stack
                        #     for card in new_stack.cards:    
                        #         selected_stack.add_card(card)

                        # selected_stack = None
                        # selected_card = None
                        # original_position = None
                        # original_mouse = 0, 0

                        # if new_stack in game_manager:
                        #     game_manager.remove(new_stack)
                        #     new_stack = None

                        # for i, stack in enumerate(game_manager):
                        #         for j, card in enumerate(stack.cards):
                        #             print(f"MU - Stack:{i}, Card: {j} - {card.name}")

        # Render all stacks
        print(f"Game Manager = {len(game_manager)}")
        game_manager = [stack for stack in game_manager if isinstance(stack, Stack) and len(stack.cards) > 0]
        for stack in game_manager:
            render.draw_stack(stack)

        pygame.display.flip()
        clock.tick(5)  # Limit to 5 FPS