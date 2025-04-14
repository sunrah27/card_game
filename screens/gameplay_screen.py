import pygame
from logic.card import WitchCard, EnemyCard
from logic.ability import witch_abilities, enemy_abilities
from logic.stack import Stack
from ui.ui_manager import Button
from ui.render import Render
from config import *

class GameplayScreen:
    def __init__(self, screen, game_state_manager):
        self.screen = screen
        self.game_state_manager = game_state_manager

        # Buttons
        self.add_card_button = Button("Add Card", 0, SCREEN_HEIGHT-100, 150, 100, self.add_card)

        self.renderer = Render(self.screen, None)
        self.stacks = []
        self.dragging_stack = None
        # self.dragging_card_offset = (0, 0)
        self.SNAP_DISTANCE = 100
        self.setup_game()
    
    def setup_game(self):
        # Create instances of cards
        witch1 = WitchCard("Fire Witch", "A fiery sorceress.", "Hot-headed and fearless.", "witch.png", (237, 81, 185), -1, 4, 1,  "Witch", 1, 400, 400, witch_abilities)
        witch2 = WitchCard("Ninja", "A sneaky ninja.", "Quiet and stealthy, hides in the shadows.", "ninja.png", (237, 181, 185), -1, 2, 2, "Witch", 1, 50, 50, witch_abilities)
        witch3 = WitchCard("Worker", "A hard worker.", "A busy body always building something.", "boy.png", (50, 50, 250), -1, 1, 4, "Witch", 1, 50, 50, witch_abilities)

        enemy = EnemyCard("Zombie", "A sneaky zombie.", "Smelly and green.", "zombine.png", (216, 57, 71), -1, 2, 1, "Enemy", 1, 210, 50, enemy_abilities)

        # Create stack
        self.stacks.extend([
            Stack(100, 100, [witch1, witch2, witch3]),
            Stack(300, 100, [enemy]),
            Stack(500, 100, [witch1, witch2, witch3]),
            Stack(5, 480, [witch1])
        ])

    
    def render(self):
        # Clear screen
        self.screen.fill(BG_COLOUR)

        # Draw buttons
        self.add_card_button.render(self.screen)

        for stack in self.stacks:
            self.renderer.draw_stack(stack)

    def handle_input(self, events):
        self.add_card_button.update()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.add_card_button.is_clicked(mouse_pos):
                    self.add_card_button.click()

                for stack in reversed(self.stacks):
                    index = stack.get_clicked_card_index(mouse_pos)
                    if index != -1:
                        self.dragging_stack = stack.split(index)
                        if self.dragging_stack:
                            self.drag_offset = (
                                mouse_pos[0] - self.dragging_stack.x,
                                mouse_pos[1] - self.dragging_stack.y
                            )
                            self.stacks.append(self.dragging_stack)
                        break

            elif event.type == pygame.MOUSEMOTION and self.dragging_stack:
                mouse_pos = pygame.mouse.get_pos()
                self.dragging_stack.update_position(mouse_pos, self.drag_offset)

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.dragging_stack:
                closest_stack = None
                min_distance = float('inf')

                for stack in self.stacks:
                    if stack == self.dragging_stack or not stack.cards:
                        continue

                    dx = self.dragging_stack.x - stack.x
                    dy = self.dragging_stack.y - (stack.y + len(stack.cards) * 30)
                    distance = (dx ** 2 + dy ** 2) ** 0.5

                    if distance < self.SNAP_DISTANCE and distance < min_distance:
                        min_distance = distance
                        closest_stack = stack

                if closest_stack:
                    for card in self.dragging_stack.cards:
                        closest_stack.add_card(card)
                    self.stacks.remove(self.dragging_stack)
                else:
                    # Optionally snap back or create new stack if desired
                    pass

                self.dragging_stack = None

        self.stacks[:] = [stack for stack in self.stacks if stack.cards]
    
    def add_card(self):
        new_x = 5
        new_y = SCREEN_HEIGHT-100-10-210

        witch1 = WitchCard("Fire Witch", "A fiery sorceress.", "Hot-headed and fearless.", "witch.png", (237, 81, 185), -1, 4, 1, "Witch", 1, new_x, new_y, witch_abilities)

        for stack in self.stacks:
            if stack.x == new_x and stack.y == new_y:
                stack.add_card(witch1)
                break
        else:
            new_stack = Stack(new_x, new_y, [witch1])
            self.stacks.append(new_stack)