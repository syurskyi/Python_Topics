class Player:

    def __init__(self, name, is_dealer=False):
        # The player has a name
        # and a hand that is initially empty
        self._name = name
        # The hand attribute is protected
        # and it doesn't have getters and setters
        # because it doesn't have to be read or set.
        # These processes are handled differently
        # by the existing methods.
        self._hand = [] 
        self._is_dealer = is_dealer

    # Read-only Properties
    @property
    def name(self):
        return self._name

    @property
    def is_dealer(self):
        return self._is_dealer 

    def draw(self, deck):
        # Take a card from the deck and add it to the hand.
        # Then, return a reference to the instance.
        self._hand.append(deck.draw())
        return self

    def show_hand(self, reveal_card=False):
        # For every card in the player's hand,
        # show the data of the card.
        if not self.is_dealer:
            for card in self._hand:
                card.show()
        # If the player is the dealer,
        # hide the value of the last card
        # unless the card should be revealed.
        else:
            for i in range(len(self._hand)-1):
                self._hand[i].show()

            # Show the hidden card or not.
            if reveal_card:
                self._hand[-1].show()
            else:
                print("X")
                
    def discard(self):
        # Discard a card and return it.
        return self._hand.pop()

    def get_hand_value(self):
        # Find the value of the current hand
        # by adding the values of the cards
        # and return the result.
        value = 0
        for card in self._hand:
            value += card.value
        return value
