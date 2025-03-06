from card import Card
import pygame

class Stack:
    """
    Represents a stack of cards.

    This class manages a collection of cards, allowing them to be stacked, 
    added, removed, and manipulated in a parent-child relationship. The 
    top-most card in the stack is considered the parent of all subsequent cards.

    Attributes:
        x (int): The x-coordinate of the stack's position.
        y (int): The y-coordinate of the stack's position.
        cards (list[Card]): A list of Card objects that are part of the stack.
    """
    def __init__(self, x, y, cards=None):
        """
        Initializes the Stack with an optional list of cards.

        Args:
            x (int): The x-coordinate of the stack's position.
            y (int): The y-coordinate of the stack's position.
            cards (list[Card], optional): A list of Card objects to initialize the stack with. Defaults to an empty list.
        """
        self.x = x
        self.y = y
        self.cards = cards if cards else []

    def __iter__(self):
        """
        Returns an iterator over the cards in the stack.

        Returns:
            iterator: An iterator over the Card objects in the stack.
        """
        return iter(self.cards)

    def __str__(self):
        # Returns a string representation of the Stack's details
        card_names = [card.name for card in self.cards]  # Assuming cards have a 'name' attribute
        return f"Stack at ({self.x}, {self.y}) with cards: {', '.join(card_names)}"

    def add_card(self, card: Card):
        """
        Adds a card to the stack. If the stack is not empty, the new card is added to the top card.

        Args:
            card (Card): The card to be added to the stack.
        """
        self.cards.append(card)
        card.x = self.x
        card.y = self.y + (len(self.cards) - 1) * 30

    def get_clicked_card_index(self, mouse_pos):
        """
        Determines the index of the card in the stack that was clicked.

        Args:
            mouse_pos (tuple[int, int]): The (x, y) coordinates of the mouse click.

        Returns:
            int: The index of the clicked card, or -1 if no card was clicked.
        """
        x, y = mouse_pos
        for i in reversed(range(len(self.cards))):
            card_y = self.y + i * 30
            card_rect = pygame.Rect(self.x, card_y, 150, 210)
            if card_rect.collidepoint(x, y):
                return i
        return -1

    def split(self, index):
        """
        Splits the stack at the specified index, creating a new stack with the cards from the given index onward.

        Args:
            index (int): The index at which to split the stack.

        Returns:
            Stack | None: A new Stack containing the split-off cards, or None if the index is out of range.
        """
        if index < 0 or index >= len(self.cards):
            return None
        new_stack = Stack(self.x, self.y + index*30, self.cards[index:])
        self.cards = self.cards[:index]
        return new_stack

    def update_position(self, mouse_pos, drag_offset):
        """
        Updates the stack's position based on mouse movement, used for dragging functionality.

        Args:
            mouse_pos (tuple[int, int]): The new mouse position (x, y).
            drag_offset (tuple[int, int]): The offset of the drag start relative to the stack's position.
        """
        self.x = mouse_pos[0] - drag_offset[0]
        self.y = mouse_pos[1] - drag_offset[1]
        for i, card in enumerate(self.cards):
            card.x = self.x
            card.y = self.y + i * 30