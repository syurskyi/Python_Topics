from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    

    numbers = list(range(0,10)) + ['Draw Two','Skip','Reverse']

    cards = [UnoCard(suit,number) for suit in SUITS for number in numbers for i in range(2 if number != 0 else 1)]

    print(len(cards))


    special_cards = ['Wild','Wild Draw Four']



    for special_card in special_cards:
        for _ in range(4):
            uno_card = UnoCard(None,special_card)
            cards.append(uno_card)


    return cards



if __name__ == "__main__":


    uno_deck = create_uno_deck()

    print(len(uno_deck))
