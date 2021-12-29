____ collections _______ namedtuple
_______ random
____ string _______ ascii_uppercase

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = r..(1, 5)

PawCard = namedtuple('PawCard', 'card action')

___ create_paw_deck(n=8):

    __ n > 26:
        raise ValueError("Number of cards can be at most 26")

    
    pawcards    # list
    ___ i __ r..(n):

        r = random.randint(1,4)
        ___ j __ r..(1,5):
            letter = chr(ord('A') + i)
            action = N..
            card = f"{letter}{j}"
            __ r __ j:
                action = random.choice(ACTIONS)


            pawcard = PawCard(card,action)
            pawcards.a..(pawcard)
    
    r.. pawcards
