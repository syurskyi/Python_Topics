from collections import namedtuple
import random
from string import ascii_uppercase

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')

def create_paw_deck(n=8):

    if n > 26:
        raise ValueError("Number of cards can be at most 26")

    
    pawcards = []
    for i in range(n):

        r = random.randint(1,4)
        for j in range(1,5):
            letter = chr(ord('A') + i)
            action = None
            card = f"{letter}{j}"
            if r == j:
                action = random.choice(ACTIONS)


            pawcard = PawCard(card,action)
            pawcards.append(pawcard)
    
    return pawcards
