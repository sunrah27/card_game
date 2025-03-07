# input_manager.py - Handles player input
#     Processes keyboard/mouse input and triggers actions.

class InputManager:
    def __init__(self):
        self.key_inputs = []  # You will eventually track keys that are pressed

    def update(self):
        """Check for any inputs. This can be expanded for keyboard/mouse."""
        print("Checking for player input...")
        # For now, let's simulate that the player pressed a key
        self.key_inputs.append("Some input")
        
    def get_inputs(self):
        return self.key_inputs
