#from inspect import stack
from card import Card

class Stack:
    """
    A class to represent a stack of cards.

    This class manages a collection of cards, allowing them to be stacked, added, 
    removed, and manipulated in a parent-child relationship. The top-most card in 
    the stack is considered the parent of all subsequent cards.

    Attributes:
        cards (list): A list of Card objects that are part of the stack.
        x (int): The x-coordinate of the stack's position.
        y (int): The y-coordinate of the stack's position.

    Methods:
        get_top_card():
            Get the top card of the stack.
        add_card(card: Card):
            Adds a card to the stack. If the stack is empty, the card is added without 
            a parent. Otherwise, the card becomes a child of the current top card.
        remove_cards(start_card: Card):
            Removes all cards from the stack starting from the given card. The stack is 
            split, and the removed cards' parent-child relationships are broken.
        from_cards(cards: list):
            Creates a new stack from a given list of Card objects. This method is used 
            when you need to create a stack from existing cards without manually adding 
            them one by one.
        update_position(mouse_pos):
            Updates the position of the stack based on mouse movement (for dragging).
    """
    def __init__(self, cards: list):
        """
        Initialize the Stack with an optional list of cards.

        Args:
            cards (list, optional): A list of Card objects to initialize the stack with.
        """
        self.cards = cards if cards else []             # Deafult to [] if no stack is passed
        self.x = self.cards[0].x if self.cards else 0   # Default to 0 if no cards
        self.y = self.cards[0].y if self.cards else 0   # Default to 0 if no cards

    def __iter__(self) -> iter:
        """
        Make the Stack iterable by iterating over the cards list.

        Returns:
            iterator: An iterator over the cards in the stack.
        """
        return iter(self.cards)

    def get_top_card(self):
        """
        Get the top card of the stack.

        Returns:
            Card: The top card, or None if the stack is empty.
        """
        if not self.cards:
            return None
        return self.cards[-1]

    def add_card(self, card: Card):
        """
        Add a card to the stack.

        Args:
            card (Card): The card to be added.
        """
        if not self.cards:
            card.parent = None  # First card in the stack
        else:
            self.cards[-1].add_child(card)  # Link to the current top card
        self.cards.append(card)
    
    def remove_cards(self, start_card: Card):
        """
        Remove cards from the stack starting from the specified card.

        Args:
            start_card (Card): The card from which to start removing.

        Returns:
            Stack: A new stack containing the removed cards.
        """
        if start_card not in self.cards:
            return None

        # Split the stack
        start_index = self.cards.index(start_card)
        removed_cards = self.cards[start_index:]
        self.cards = self.cards[:start_index]

        # Break parent-child relationships
        if self.cards:
            self.cards[-1].children = []
        for card in removed_cards:
            card.parent = None
        
        return Stack.from_cards(removed_cards)

    def update_position(self, mouse_pos):
        """
        Update the position of the stack based on mouse movement.

        This method allows the stack to follow the mouse during dragging, updating the
        stack's position on the screen. Each card in the stack will also be repositioned 
        accordingly.

        Args:
            mouse_pos (tuple): A tuple representing the current position of the mouse 
                               (x, y) used to reposition the stack.
        """
        # Update the stack's position based on mouse input (dragging)
        self.x = mouse_pos[0] - self.cards[0].width // 2
        self.y = mouse_pos[1] - self.cards[0].height // 8

        # Update the position of all cards in the stack
        for card in self.cards:
            card.x = self.x
            card.y = self.y

    @staticmethod
    def from_cards(cards: list):
        """
        Create a new Stack from a list of cards.

        This static method is useful for creating a stack from an existing set of cards
        without needing to manually add each card.

        Args:
            cards (list): The list of Card objects.

        Returns:
            Stack: A new stack initialized with the given cards.
        """
        stack = Stack()
        for card in cards:
            stack.add_card(card)
        return stack