# Python 2.7

___ find_name(amount_of_cards
    #amount_of_cards is a wasted variable required by CodeAbbey.
    answer    # list
    cards = [i..(x) ___ x __ raw_input().s.. ]
    suits =  'Clubs', 'Spades', 'Diamonds', 'Hearts' 
    ranks =  '2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack','Queen', 'King', 'Ace' 
    ___ card __ cards:
        suit_number = card / 13
        suit = suits[suit_number]
        
        rank_number = card % 13
        rank = ranks[rank_number]

        answer.a..('{0}-of-{1}'.f..(rank, suit))
    print(' '.j..(answer))
find_name(input())
