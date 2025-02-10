import pygame

class Card:
    """
    Base class for all cards in the game.

    Attributes:
        name (str): Name of the card.
        desc (str): Description of the card.
        flavour (str): Additional flavour text for the card.
        sprite (str): Path or name of the graphical representation associated with the card.
        colour (tuple): RGB tuple representing the colour of the card.
        value (int): Value of the card, used for various game mechanics.
        hp (int): Hit points of the card, determining its durability.
        atk (int): Attack value of the card, determining its offensive power.
        card_type (str): The type of the card (e.g., Witch, Resource, Enemy).
        stack (int): Whether the card can be stacked with others (1 = yes, 0 = no).
        x (int): x-coordinate of the card's position on the game board.
        y (int): y-coordinate of the card's position on the game board.
        width (int): Width of the card.
        height (int): Height of the card.
        rect (pygame.Rect): Rect object representing the card's position and dimensions.

    Methods:
        use(): 
            Placeholder method for card actions. Intended to be overridden by subclasses.
        is_dead():
            Checks if the card's HP is zero or less, indicating it's dead.
        add_child(child: Card):
            Adds a card to the stack, setting this card as the parent for the child card.
        remove_child(child: Card):
            Removes a child card from the stack and detaches it from the parent card.
        update_rect():
            Updates the position of the card's rectangle based on its current x and y coordinates.
    """
    def __init__(self, name: str, desc: str, flavour: str, sprite: str, colour:tuple, value: int, hp: int, atk: int, card_type: str, stack: int, x: int, y: int):
        self.name = name
        self.desc = desc
        self.flavour = flavour
        self.sprite = sprite
        self.colour = colour
        self.value = value
        self.hp = hp
        self.atk = atk
        self.card_type = card_type
        self.stack = stack
        self.x = x
        self.y = y
        self.width = 150
        self.height = 210
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def use(self):
        pass

    def is_dead(self):
        return self.hp <= 0
    
    def update_rect(self):
        self.rect.topleft = (self.x, self.y)


class WitchCard(Card):
    """
    Class for Witch cards, representing units controlled by the player.

    Inherits from the `Card` class and adds additional attributes and methods specific to Witch cards.

    Attributes:
        max_hp (int): Maximum HP of the Witch card, used to track the card's health limits.
        shield (int): Amount of shield protection on the Witch card.
        abilities (list): List of abilities that the Witch card can perform.

    Methods:
        perform_ability(ability_name: str, *args, **kwargs):
            Finds and executes an ability by its name. This method searches through the Witch's 
            abilities and executes the matching one if found.
    """
    def __init__(self, name: str, desc: str, flavour: str, sprite: str, colour: tuple, value: int, hp: int, atk: int, card_type: str, stack: int, x: int, y: int, abilities: list):
        super().__init__(name, desc, flavour, sprite, colour, value, hp, atk, card_type, stack, x, y)
        self.max_hp = hp
        self.shield = 0
        self.abilities = abilities or []

    def perform_ability(self, ability_name: str, *args, **kwargs):
        for ability in self.abilities:
            if ability_name == ability_name:
                ability.execute(self, *args, **kwargs)
                return

class EnemyCard(Card):
    """
    Class for Enemy cards, representing units that the player needs to interact with or defeat.

    Inherits from the `Card` class and adds additional attributes and methods specific to Enemy cards.

    Attributes:
        max_hp (int): Maximum HP of the Enemy card, used to track the card's health limits.
        shield (int): Amount of shield protection on the Enemy card.
        abilities (list): List of abilities that the Enemy card can perform.

    Methods:
        perform_ability(ability_name: str, *args, **kwargs):
            Finds and executes an ability by its name. This method searches through the Enemy's 
            abilities and executes the matching one if found.
    """
    def __init__(self, name: str, desc: str, flavour: str, sprite: str, colour: tuple, value: int, hp: int, atk: int, card_type: str, stack: int, x: int, y: int, abilities: list):
        super().__init__(name, desc, flavour, sprite, colour, value, hp, atk, card_type, stack, x, y)
        self.max_hp = hp
        self.shield = 0
        self.abilities = abilities or []

    def perform_ability(self, ability_name: str, *args, **kwargs):
        for ability in self.abilities:
            if ability_name == ability_name:
                ability.execute(self, *args, **kwargs)
                return