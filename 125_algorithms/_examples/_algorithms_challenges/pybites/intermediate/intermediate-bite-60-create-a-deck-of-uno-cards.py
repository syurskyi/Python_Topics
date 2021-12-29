from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    inventory = {
        '0': 1,
        '1': 2,
        '2': 2,
        '3': 2,
        '4': 2,
        '5': 2,
        '6': 2,
        '7': 2,
        '8': 2,
        '9': 2,
        'Draw Two': 2,
        'Skip': 2,
        'Reverse': 2,
    }
    deck = []
    for s in SUITS:
        for k, v in inventory.items():
            for i in range(0, v):
                card = UnoCard(s, k)
                deck.append(card)
    for i in range(0,4):
        card = UnoCard(None, 'Wild')
        deck.append(card)
    for i in range(0,4):
        card = UnoCard(None, 'Wild Draw Four')
        deck.append(card)
    return deck

print(create_uno_deck())

