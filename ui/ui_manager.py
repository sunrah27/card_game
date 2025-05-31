import pygame

class UIManager:
    def __init__(self, screen):
        # UI elements go here, for now, we are just simple placeholder
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

    def __init__(self, text: str, x: int, y: int, width: int, height: int, action, t_normal: tuple = None, t_hover: tuple = None, t_pressed:tuple = None, bg_normal: tuple = None, bg_hover: tuple = None, bg_pressed: tuple = None):
        self.label = text
        self.rect = pygame.Rect(x, y, width, height)                      # Button's position and size
        self.action = action                                              # Function to execute when clicked
        self._font_cache = {}
        self.t_normal = t_normal if t_normal else (255, 255, 255)         # Default normal color
        self.t_hover = t_hover if t_hover else (170, 170, 170)            # Default hover color
        self.t_pressed = t_pressed if t_pressed else (100, 100, 100)      # Default pressed color
        self.bg_normal = bg_normal if bg_normal else (0, 0, 0, 0)         # Default background color
        self.bg_hover = bg_hover if bg_hover else (0, 0, 0, 0)            # Default background hover color
        self.bg_pressed = bg_pressed if bg_pressed else (0, 0, 0, 0)      # Default background pressed color
    
    def update(self):
        """Check if the mouse is over the button and if it's clicked."""
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        hovering = self.rect.collidepoint(mouse_pos)
        
        self.is_hovered = hovering                                        # For hover state
        self.is_pressed = hovering and mouse_pressed[0]                   # For hover and pressed state

        if hovering:
            if mouse_pressed[0] and not self._was_clicked:
                self._was_clicked = True
            elif not mouse_pressed[0] and self._was_clicked:
                self.click()
                self._was_clicked = False
        else:
            self._was_clicked = False
    
    def render(self, screen):
        """Render the button."""
        button_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        
        """Choose buttons colour based on state"""
        if getattr(self, 'is_pressed', False):
            colour = self.t_pressed
            button_surface.fill(self.bg_pressed)
        elif getattr(self, 'is_hovered', False):
            colour = self.t_hover
            button_surface.fill(self.bg_hover)
        else:
            colour = self.t_normal
            button_surface.fill(self.bg_normal)

        screen.blit(button_surface, self.rect.topleft)

        if 36 not in self._font_cache:
            self._font_cache[36] = pygame.font.Font(None, 36)       # Cache the font object for reuse
        font = self._font_cache[36]                                 # Use the cached font object
        text = font.render(self.label, True, (colour))              # Render text
        
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