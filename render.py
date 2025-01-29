import pygame
from card import Card

class Render:
    def __init__(self, screen):
        self.screen = screen

    def draw_stack(self, stack):
        """
        Calls the draw_card() method to render the card stacks.
        """
        if not stack.cards:  # Check if there are no cards in the stack
            print("Stack is empty!")
        else:
            for i, card in enumerate(stack):
                card.y = stack.y + (i * 30)
                card.update_rect()
                self.draw_card(card, i)

    def draw_card(self, card: Card, i=0):
        """
        Renders the card template on the screen using the card's details.
        """
        border = 2
        offset = 12
        border_radius = 7
        card_colour = card.colour
        header_color = (0, 0, 0, 180)  # Black with transparency
        shadow_colour = (0, 0, 0, 100)
        rect_width = 150
        rect_height = rect_width * 1.4
        x, y = card.x, card.y
        header_font = pygame.font.Font(None, 28)
        stat_font = header_font

        # Create shadow
        shadow_rect = pygame.Rect(x + 7, y + 7, rect_width, rect_height)
        shadow_surface = pygame.Surface((shadow_rect.width, shadow_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(shadow_surface, shadow_colour, shadow_surface.get_rect(), border_radius=border_radius)
        self.screen.blit(shadow_surface, shadow_rect.topleft)

        # Draw the card
        pygame.draw.rect(self.screen, card_colour, (x, y, rect_width, rect_height), 0, border_radius)

        # Header and body sections
        header_surface = pygame.Surface((rect_width - 2 * offset, rect_height - 2 * offset), pygame.SRCALPHA)
        header_surface.fill(header_color)
        self.screen.blit(header_surface, (x + offset, y + offset))

        # Draw the body
        pygame.draw.rect(self.screen, card_colour, (x + offset + border, y + border + offset + 30, rect_width - 2 * offset - 2 * border, rect_height - 2 * offset - 2 * border - 30))
        
        # Render sprite image here
        image = pygame.image.load(f"assets/{card.sprite}").convert_alpha()
        # get centre of the card
        centre_x = card.x + rect_width // 2
        cantre_y = card.y + rect_height // 2
        # resize image to 100 x 100
        scaled_image = pygame.transform.scale(image, (100, 100))
        # calculate image start position
        self.screen.blit(scaled_image, (centre_x - 50, cantre_y - 50))
        # draw image

        # Calculate position to center the text horizontally and vertically in the header area
        text_surface = header_font.render(card.name, True, (255, 255, 255))
        text_width, text_height = header_font.size(card.name)
        text_x = x + offset + (rect_width - 2 * offset - text_width) // 2
        text_y = y + offset + (30 - text_height) // 2
        self.screen.blit(text_surface, (text_x, text_y + 1))

        # Atk/Value Text
        if card.value == -1:
            av_text = stat_font.render(str(card.atk), True, (255, 255, 255))
            av_text_width, av_text_height = stat_font.size(str(card.atk))
        else:
            av_text = stat_font.render(str(card.value), True, (255, 255, 255))
            av_text_width, av_text_height = stat_font.size(str(card.value))
        left_x = x + offset + border + 5
        bottom_y = y + rect_height - offset - border - av_text_height - 5
        self.screen.blit(av_text, (left_x, bottom_y))

        # check card for HP
        if card.hp != -1:
            hp_text = stat_font.render(str(card.hp), True, (255, 255, 255))
            hp_text_width, hp_text_height = stat_font.size(str(card.hp))
            right_x = x + rect_width - offset - border - hp_text_width - 5
            self.screen.blit(hp_text, (right_x, bottom_y))
        else:
            # Add sprite for building image
            pass

        # check card for shield
        if card.shield > 0:
            shield_text = stat_font.render(str(card.shield), True, (255, 255, 255))
            shield_text_x = rect_width - offset - border - 2
            shield_text_y = rect_height - offset - border - 20
            self.screen.blit(shield_text, (shield_text_x, shield_text_y))
    
    def get_top_rect(mouse_pos, game_manager):
        for stack in reversed(game_manager):            # Check from the topmost stack to bottommost stack
            for card in reversed(stack.cards):          # Check from top card in the stack to the bottom card
                if card.rect.collidepoint(mouse_pos):
                    return stack, card                  # Return the card, not just the rect
        return None, None