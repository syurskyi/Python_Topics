from collections ______ defaultdict

___ poker(hands
    """poker determines the best poker hand from a set of hands"""
    best_hands, best_score =   # list, None
    ___ hand __ hands:
        score = score_hand(hand)
        __ best_score __ None or best_score < score:
            best_hands, best_score = [hand], score
        ____ best_score __ score:
            best_hands.append(hand)
    r_ best_hands

___ score_hand(hand
    """score_hand scores a poker hand based on it's type and the cards"""
    suits, ranks = get_suits_and_ranks(hand)
    sorted_ranks = sorted(ranks.keys())
    kinds = sorted(list(ranks.values()), reverse=True)

    flush = al.(suit __ suits[0] ___ suit __ suits)
    straight = al.(sorted_ranks[0] + i __ rank ___ i, rank __ enumerate(sorted_ranks))

    __ sorted_ranks __ [2,3,4,5,14]:
        straight, ranks = True, {1:1, 2:1, 3:1, 4:1, 5:1}

    __ flush and straight:
        score = 8
    ____ kinds __ [4,1]:
        score = 7
    ____ kinds __ [3,2]:
        score = 6
    ____ flush:
        score = 5
    ____ straight:
        score = 4
    ____ kinds __ [3,1,1]:
        score = 3
    ____ kinds __ [2,2,1]:
        score = 2
    ____ kinds __ [2,1,1,1]:
        score = 1
    ____
        score = 0

    hand = sorted(ranks.items(), key=lambda r: (-r[1], -r[0]))
    r_ [score] + [v ___ v,c __ hand ___ _ __ range(c)]

___ get_suits_and_ranks(hand
    """get_suits_and_ranks splits a hand into suits and ranks"""
    suits, ranks =   # list, defaultdict(int)
    ___ card __ hand:
        suit, rank = card[-1], card[:-1]
        suits.append(suit)
        ranks[ convert_rank(rank) ] += 1
    r_ suits, ranks

"""convert_rank converts a rank to an integer"""
convert_rank = lambda c: '--23456789TJQKA'.index(c)


