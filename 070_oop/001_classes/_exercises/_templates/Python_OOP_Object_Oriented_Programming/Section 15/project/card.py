class Card:
    
    def __init__(self, suit, value):
        # The card has a suit and a value
        # as instance attributes.
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def show(self):
        # A print statement that will show the data of the card.
        print(f"{self._value} of {self._suit}")
