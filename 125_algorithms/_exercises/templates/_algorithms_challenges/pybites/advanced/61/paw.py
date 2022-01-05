____ c.. _______ n..
_______ r__
____ s__ _______ a..

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = r..(1, 5)

PawCard = n..('PawCard', 'card action')

___ create_paw_deck(n=8):

    __ n > 26:
        r.. ValueError("Number of cards can be at most 26")

    
    pawcards    # list
    ___ i __ r..(n):

        r = r__.randint(1,4)
        ___ j __ r..(1,5):
            letter = chr(o..('A') + i)
            action = N..
            card = f"{letter}{j}"
            __ r __ j:
                action = r__.choice(ACTIONS)


            pawcard = PawCard(card,action)
            pawcards.a..(pawcard)
    
    r.. pawcards
