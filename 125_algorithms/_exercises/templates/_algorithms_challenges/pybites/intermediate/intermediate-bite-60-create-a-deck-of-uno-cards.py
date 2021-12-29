____ collections _______ n..

SUITS = 'Red Green Yellow Blue'.s..

UnoCard = n..('UnoCard', 'suit name')


___ create_uno_deck():
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
    deck    # list
    ___ s __ SUITS:
        ___ k, v __ inventory.items():
            ___ i __ r..(0, v):
                card = UnoCard(s, k)
                deck.a..(card)
    ___ i __ r..(0,4):
        card = UnoCard(N.., 'Wild')
        deck.a..(card)
    ___ i __ r..(0,4):
        card = UnoCard(N.., 'Wild Draw Four')
        deck.a..(card)
    r.. deck

print(create_uno_deck())

