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
        self.renderer = Render(self.screen, None)
        self.stacks = []
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

        self.add_card_button = Button("Add Card", 0, SCREEN_HEIGHT-100, 150, 100, None)
    
    def render(self):
        self.screen.fill(BG_COLOUR)
        self.renderer.draw(self.stacks)
        # self.add_card_button.draw(self.screen)
        pygame.display.flip()