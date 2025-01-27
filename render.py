import pygame

class Render:
    def __init__(self, screen):
        self.screen = screen

    def draw_card(self, card):
        """
        Renders the card template on the screen using the card's details.
        """
        border = 2
        offset = 12
        border_radius = 7
        card_colour = card.colour  # White, could be dynamic based on card type
        header_color = (0, 0, 0, 180)  # Black with transparency
        shadow_colour = (0, 0, 0, 70)
        rect_width = 150
        rect_height = rect_width * 1.4
        x = card.x
        y = card.y

        # Create shadow
        shadow_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
        shadow_surface.fill(shadow_colour)
        self.screen.blit(shadow_surface, (x + 7, y + 7))

        # Draw the card
        pygame.draw.rect(self.screen, card_colour, (x, y, rect_width, rect_height), 0, border_radius)

        # Header and body sections
        header_surface = pygame.Surface((rect_width - 2 * offset, rect_height - 2 * offset), pygame.SRCALPHA)
        header_surface.fill(header_color)
        self.screen.blit(header_surface, (x + offset, y + offset))

        pygame.draw.rect(self.screen, card_colour, (x + offset + border, y + border + offset + 30, rect_width - 2 * offset - 2 * border, rect_height - 2 * offset - 2 * border - 30))
        
        # You can draw card-specific details here (name, description, etc.)
        # This is where card text or images would go, based on the card type

        # Calculate position to center the text horizontally and vertically in the header area
        font = pygame.font.Font(None, 28)
        text_surface = font.render(card.name, True, (255, 255, 255))
        text_width, text_height = font.size(card.name)
        text_x = x + offset + (rect_width - 2 * offset - text_width) // 2
        text_y = y + offset + (30 - text_height) // 2

        # Blit the text surface at the calculated position
        self.screen.blit(text_surface, (text_x, text_y + 1))

    # You can add other functions for drawing different game elements (e.g., board, enemies, etc.)
