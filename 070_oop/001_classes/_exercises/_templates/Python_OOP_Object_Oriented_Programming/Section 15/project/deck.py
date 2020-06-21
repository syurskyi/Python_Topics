import random
from card import Card

class Deck:

    # The four types of suits for the card.
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    
    def __init__(self):
        # The deck starts with an empty list of cards.
        # It is protected and it doesn't have a getter
        # setter because they are not needed.
        self._cards = []
        # Then this is populated when we build the deck.
        self.build()

    def build(self):
        # For every suit and value, create the corresponding cards
        # with a value from 1 to 11 (the end value is not included in range()).
        for suit in Deck.suits:
            for value in range(1, 12):
                self._cards.append(Card(suit, value))

    def show(self):
        # For every card in the list of cards of the deck,
        # show the information of the card.
        for card in self._cards:
            card.show()

    def shuffle(self):
        # Use the Fisher-Yates algorithm to shuffle the deck.
        for i in range(len(self._cards)-1, 0, -1):
            rand = random.randint(0, i)
            self._cards[i], self._cards[rand] = self._cards[rand], self._cards[i]

    def draw(self):
        # Remove the card from the deck (if the deck is not empty)
        # and return the card.
        if self._cards:
            return self._cards.pop()
