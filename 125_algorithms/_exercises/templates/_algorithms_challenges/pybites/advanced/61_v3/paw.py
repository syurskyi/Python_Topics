_______ r__
____ c.. _______ n..
____ m__ _______ ceil

LETTER_A_CODE = 65

ACTIONS =  'draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction'
NUMBERS = r..(1, 5)

PawCard = n..('PawCard', 'card action')


___ create_paw_deck(n=8
    __ n > 26:
        r.. V...('maximum of 26 suits')
    deck    # list
    ___ suit __ r..(n
        deck.extend _*{chr(LETTER_A_CODE + suit)}{x}' ___ x __ NUMBERS)
    actions = l..((ACTIONS * c.. n / 4[:n]) + ([N..] * 3 * n)
    r__.shuffle(actions)
    r.. [PawCard(card, action) ___ card, action __ z..(deck, actions)]
