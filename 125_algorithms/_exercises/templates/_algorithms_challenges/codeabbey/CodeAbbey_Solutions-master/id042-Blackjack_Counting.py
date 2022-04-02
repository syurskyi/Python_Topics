# Python 2.7

___ blackjack_counter(games
    answer    # list
    values = {
        '2':2,    '3':3,    '4':4,
        '5':5,    '6':6,    '7':7,
        '8':8,    '9':9,
        'T':10,   'J':10,   'Q':10,
        'K':10,   'A':11
        }
    
    ___ game __ r..(games
        cards = [x ___ x __ raw_input().s.. ]
        total, ace_count = 0, 0
        
        ___ card __ cards:
            total += values[card]
            __ card __ 'A':
                ace_count += 1
                
        w.... total > 21 a.. ace_count > 0:
            total -= 10
            ace_count -= 1

        __ total > 21:
            answer.a..('Bust')
        ____:
            answer.a..(s..(total))

    print(' '.j..(answer))
blackjack_counter(input())
