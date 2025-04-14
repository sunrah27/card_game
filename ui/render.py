import pygame
from logic.card import Card

class Render:
    def __init__(self, screen, button) -> None:
        self.screen = screen
        self.button = button

    def draw_ui(self):
        self.button.draw(self.screen)

    def draw_stack(self, stack) -> None:
        """
        Calls the draw_card() method to render the card stacks.
        """
        if stack.cards:
            for i, card in enumerate(stack.cards):
                if card in stack.cards:
                    card.x = stack.x
                    card.y = stack.y + (i * 30)
                    card.update_rect()
                self.draw_card(card)

    def draw_card(self, card: Card) -> None:
        """
        Renders the card template on the screen using the card's details.
        """
        # Original rendering logic below
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
        xx = x + offset + border
        yy = y + border + offset + 30
        wwidth = rect_width - 2 * offset - 2 * border
        hheight = rect_height - 2 * offset - 2 * border - 30
        pygame.draw.rect(self.screen, card_colour, (xx, yy, wwidth, hheight))
        
        # Render sprite image
        try:
            image = pygame.image.load(f"assets/{card.sprite}").convert_alpha()
            scaled_image = pygame.transform.scale(image, (100, 100))
            self.screen.blit(scaled_image, (x + rect_width//2 - 50, y + rect_height//2 - 50))
        except Exception as e:
            print(f"Error loading image: {e}")

        # Card name
        text_surface = header_font.render(card.name, True, (255, 255, 255))
        text_width, text_height = header_font.size(card.name)
        text_x = x + offset + (rect_width - 2 * offset - text_width) // 2
        text_y = y + offset + (30 - text_height) // 2
        self.screen.blit(text_surface, (text_x, text_y + 1))

        # Atk/Value Text
        if card.value == -1:
            av_text = stat_font.render(str(card.atk), True, (255, 255, 255))
        else:
            av_text = stat_font.render(str(card.value), True, (255, 255, 255))
        left_x = x + offset + border + 5
        bottom_y = y + rect_height - offset - border - stat_font.get_height() - 5
        self.screen.blit(av_text, (left_x, bottom_y))

        # HP display
        if card.hp != -1:
            hp_text = stat_font.render(str(card.hp), True, (255, 255, 255))
            right_x = x + rect_width - offset - border - hp_text.get_width() - 5
            self.screen.blit(hp_text, (right_x, bottom_y))

        # Shield display
        if card.shield > 0:
            shield_text = stat_font.render(str(card.shield), True, (255, 255, 255))
            shield_text_x = x + rect_width - offset - border - shield_text.get_width() - 5
            shield_text_y = y + offset + 5
            self.screen.blit(shield_text, (shield_text_x, shield_text_y))