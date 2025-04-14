import pygame

class UIManager:
    def __init__(self, screen):
        # UI elements go here, for now, we are just holding simple placeholder
        self.screen = screen
        self.ui_elements = []
    
    def add_ui_element(self, element):
        """Add a UI element to the list."""
        self.ui_elements.append(element)
    
    def update(self):
        """Update all UI elements. Pkaceholder for now."""
        for element in self.ui_elements:
            element.update()
    
    def render(self):
        """Render all UI elements. Placeholder for now."""
        for element in self.ui_elements:
            element.render(self.screen) 

class Button: 
    """
    Simple class to represent a button.
    text (str): The text to display on the button.
    action (function): The function to call when the button is clicked.
    x (int): The x-coordinate of the button.
    y (int): The y-coordinate of the button.
    width (int): The width of the button.
    height (int): The height of the button.
    action (function): The function to execute when the button is clicked.
    """

    def __init__(self, text: str, x: int, y: int, width: int, height: int, action):
        self.label = text
        self.rect = pygame.Rect(x, y, width, height)            # Button's position and size
        self.action = action                                    # Function to execute when clicked
        self._font_cache = {}
    
    def update(self):
        """Check if the mouse is over the button and if it's clicked."""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            if pygame.mouse.get_pressed()[0]:
                self.click()
    
    def render(self, screen):
        """Render the button."""
        button_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        button_surface.fill((0, 0, 0, 0))
        screen.blit(button_surface, self.rect.topleft)

        if 36 not in self._font_cache:
            self._font_cache[36] = pygame.font.Font(None, 36)       # Cache the font object for reuse
        font = self._font_cache[36]                                 # Use the cached font object
        text = font.render(self.label, True, (0,0,0))               # Render text
        
        # Center the text on the button rect
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def click(self):
        """Simulate a button click."""
        print(f"Button clicked: {self.label}")
        self.action()   # Call the action associated with the button

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def draw(self, surface):
        self.render(surface)