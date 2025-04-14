import pygame
from logic.card import WitchCard, EnemyCard
from logic.ability import witch_abilities, enemy_abilities
from logic.stack import Stack
from config import *
from ui.ui_manager import Button

class GameplayScreen:
    def __init__(self, screen, game_state_manager):
        self.screen = screen
        self.game_state_manager = game_state_manager
        self.screen.fill(BG_COLOUR)

        font = pygame.font.Font(None, 32)
        self.add_card_button = Button(0, SCREEN_HEIGHT-100, 150, 100, (200,0,0), "Add Card", font)

        self.cards = []
        self.stacks = []
        self.selected_card = None
        self.offset_x = 0
        self.offset_y = 0
        self.setup_game()
    
    def setup_game(self):
        # Create instances of cards
        witch1 = WitchCard("Fire Witch", "A fiery sorceress.", "Hot-headed and fearless.", "witch.png", (237, 81, 185), -1, 4, 1,  "Witch", 1, 400, 400, witch_abilities)
        witch2 = WitchCard("Ninja", "A sneaky ninja.", "Quiet and stealthy, hides in the shadows.", "ninja.png", (237, 181, 185), -1, 2, 2, "Witch", 1, 50, 50, witch_abilities)
        witch3 = WitchCard("Worker", "A hard worker.", "A busy body always building something.", "boy.png", (50, 50, 250), -1, 1, 4, "Witch", 1, 50, 50, witch_abilities)

        enemy = EnemyCard("Zombie", "A sneaky zombie.", "Smelly and green.", "zombine.png", (216, 57, 71), -1, 2, 1, "Enemy", 1, 210, 50, enemy_abilities)

        # Create stack
        self.stacks.append(
            Stack(100, 100, [witch1, witch2, witch3]),
            Stack(300, 100, [enemy]),
            Stack(500, 100, [witch1, witch2, witch3]),
            Stack(5, 480, [witch1])
        )