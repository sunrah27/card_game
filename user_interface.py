import pygame
from card import WitchCard
from ability import witch_abilities
from stack import Stack
from config import *

class UIButton:
    def __init__(self, x, y, width, height, colour, text, font, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.colour = colour
        self.font = font
        self.text = text
        self.action = action
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect, border_radius=0)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def add_card_click(self, game_manager):
        new_x = 5
        new_y = SCREEN_HEIGHT-100-10-210

        witch1 = WitchCard("Fire Witch", "A fiery sorceress.", "Hot-headed and fearless.", "witch.png", (237, 81, 185), -1, 4, 1, "Witch", 1, new_x, new_y, witch_abilities)

        for stack in game_manager:
            if stack.x == new_x and stack.y == new_y:
                stack.add_card(witch1)
                print(f"Added card to existing stack at ({stack.x}, {stack.y})")
                break
        else:
            new_stack = Stack(new_x, new_y, [witch1])
            game_manager.append(new_stack)
            print(f"Added card to new stack at ({new_x}, {new_y})")