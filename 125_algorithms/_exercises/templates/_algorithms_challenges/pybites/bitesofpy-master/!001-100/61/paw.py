______ random
from collections ______ namedtuple
from ma__ ______ ceil

LETTER_A_CODE = 65

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')


___ create_paw_deck(n=8
    __ n > 26:
        raise ValueError('maximum of 26 suits')
    deck = []
    ___ suit in range(n
        deck.extend(f'{chr(LETTER_A_CODE + suit)}{x}' ___ x in NUMBERS)
    actions = list((ACTIONS * ceil(n / 4))[:n]) + ([None] * 3 * n)
    random.shuffle(actions)
    r_ [PawCard(card, action) ___ card, action in zip(deck, actions)]
