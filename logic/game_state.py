class GameStateManager:
    def __init__(self, screen):
        self.screen = screen
        self.screens = {}
        self.current_state = None

    def add_screen(self, state_name, screen):
        """Add a screen to the manager."""
        self.screens[state_name] = screen

    def change_state(self, state_name):
        """Change the current active screen."""
        self.current_state = state_name

    def render(self):
        """Render the current screen."""
        if self.current_state:
            screen = self.screens[self.current_state]
            screen.render()

    def handle_input(self, events):
        """Handle input events for the current screen."""
        if self.current_state:
            screen = self.screens[self.current_state]
            if hasattr(screen, 'handle_input'):
                screen.handle_input(events)