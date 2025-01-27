class Card:
    """
    Base class for all cards in the game.

    Arguments:
        key (str): Unique identifier for the card.
        name (str): Name of the card.
        desc (str): Description of the card.
        flavour (str): Additional flavour text.
        sprite (str): Graphical representation associated with the card.
        colour (tuple): Colour of the card (usually an RGB tuple).
        value (int): Value of the card (used for game mechanics).
        hp (int): Hit points of the card.
        atk (int): Attack value of the card.
        card_type (str): The type of card (e.g., Witch, Resource, Enemy, etc.).
        stack (int): Can this card be stacked with other cards (1 = yes, 0 = no)?
        x (int): x position of the card on the game board.
        y (int): y position of the card on the game board.

    Methods:
        use():
            Performs the card's action. This method is intended to be overridden by 
            subclasses to implement specific card behaviors.
        is_dead():
            When Hp = 0 destroy card.
        add_child(child):
            Adds a card on top of this card (stacking).
        remove_child(child):
            Removes a card from this card's stack.
    """
    def __init__(self, key: str, name: str, desc: str, flavour: str, sprite: str, colour:tuple, value: int, hp: int, atk: int, card_type: str, stack: int, x: int, y: int):
        self.key = key
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
        self.parent = None
        self.children = []
    
    def use(self):
        pass

    def is_dead(self):
        return self.hp <= 0

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
            child.parent = None

class WitchCard(Card):
    """
    Class for all units the player controls.

    Arguments:
        max_hp (int): Max Hp value for the card.
        abilieies (list): List of abilities the card can perform.
    
    Methods:
        perform_ability(ability_name):
            Find and execute an ability by name.
    """
    def __init__(self, key: str, name: str, desc: str, flavour: str, sprite: str, colour: tuple, value: int, hp: int, atk: int, card_type: str, stack: int, x: int, y: int, abilities: list):
        super().__init__(key, name, desc, flavour, sprite, colour, value, hp, atk, card_type, stack, x, y)
        self.max_hp = hp
        self.abilities = abilities or []
    
    def perform_ability(self, ability_name: str, *args, **kwargs):
        for ability in self.abilities:
            if ability_name == ability_name:
                ability.execute(self, *args, **kwargs)
                return

class EnemyCard(Card):
    """
    Class for all units the player controls.

    Arguments:
        max_hp (int): Max Hp value for the card.
        abilieies (list): List of abilities the card can perform.
        
    Methods:
        perform_ability(ability_name):
            Find and execute an ability by name.
    """
    def __init__(self, key: str, name: str, desc: str, flavour: str, sprite: str, colour: tuple, value: int, hp: int, atk: int, card_type: str, stack: int, x: int, y: int, abilities: list):
        super().__init__(key, name, desc, flavour, sprite, colour, value, hp, atk, card_type, stack, x, y)
        self.max_hp = hp
        self.abilities = abilities or []
    
    def perform_ability(self, ability_name: str, *args, **kwargs):
        for ability in self.abilities:
            if ability_name == ability_name:
                ability.execute(self, *args, **kwargs)
                return