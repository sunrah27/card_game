"""insert docstring for Card import"""
from card import Card

class Stack:
    """
    A class to represent a stack of cards.

    This class manages a collection of cards, allowing them to be stacked, added, 
    removed, and manipulated in a parent-child relationship. The top-most card in 
    the stack is considered the parent of all subsequent cards.

    Attributes:
        cards (list): A list of Card objects that are part of the stack.

    Methods:
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
    """
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        if not self.cards:
            card.parent = None  # First card in the stack
        else:
            self.cards[-1].add_child(card)  # Link to the current top card
        self.cards.append(card)
    
    def remove_cards(self, start_card: Card):
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
    
    @staticmethod
    def from_cards(cards):
        stack = Stack()
        for card in cards:
            stack.add_card(card)
        return stack
    
    def is_overlapping(card, stack):
        # Check if the card's position is near the stack's top card
        if not stack.cards:
            return False

        top_card = stack.cards[-1]
        card_width, card_height = 70, 100  # Example dimensions
        return (
            abs(card.x - top_card.x) < card_width / 2 and
            abs(card.y - top_card.y) < card_height / 2
        )