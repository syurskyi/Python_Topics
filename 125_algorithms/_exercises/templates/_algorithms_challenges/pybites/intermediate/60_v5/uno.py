____ collections _______ n..

SUITS = 'Red Green Yellow Blue'.s..

UnoCard = n..('UnoCard', 'suit name')

SUIT_VALUES = '1,2,3,4,5,6,7,8,9,Draw Two,Skip,Reverse'.s..(',')


___ create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    cards    # list
    ___ suit __ SUITS:
        add_suit(cards.a.., suit)
    ___ value __ 'Wild,Wild Draw Four'.s..(',') * 4:
        cards.a..(UnoCard(N.., value))
    r.. cards


___ add_suit(cards_append, suit: s..):
    cards_append(UnoCard(suit, '0'))
    ___ value __ SUIT_VALUES:
        cards_append(UnoCard(suit, value))
        cards_append(UnoCard(suit, value))
