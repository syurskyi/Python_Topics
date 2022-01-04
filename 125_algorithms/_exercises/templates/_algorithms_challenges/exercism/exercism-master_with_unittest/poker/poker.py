STRAIGHT_FLUSH = 800
FOUR_OF_A_KIND = 700
FULL_HOUSE = 600
FLUSH = 500
STRAIGHT = 400
THREE_OF_A_KIND = 300
TWO_PAIR = 200
ONE_PAIR = 100
HIGH_CARD = 0


c_ Poker:
    ___ - , hands):
        hands = [Hand(hand) ___ hand __ hands]

    ___ best_hand
        r.. [hand.hand ___ hand, score __ l..(
            scores().i.. __ score __ best_score()]

    ___ best_score
        r.. max(scores(), key=scores().get).score()

    ___ scores
        r.. {hand: hand.score() ___ hand __ hands}


c_ Hand:
    ___ - , hand):
        hand = hand
        cards = [Card(card) ___ card __ hand]
        ranks = [card.rank ___ card __ cards]
        suits = [card.suit ___ card __ cards]

    ___ score
        __ straight_flush():
            r.. STRAIGHT_FLUSH + high_card()
        ____ four_of_a_kind():
            r.. FOUR_OF_A_KIND + rank_of_card_with_highest_occurence()
        ____ full_house():
            r.. FULL_HOUSE + rank_of_card_with_highest_occurence()
        ____ flush():
            r.. FLUSH + high_card()
        ____ straight():
            r.. STRAIGHT + high_card()
        ____ three_of_a_kind():
            r.. THREE_OF_A_KIND + rank_of_card_with_highest_occurence()
        ____ two_pair():
            r.. TWO_PAIR + high_card()
        ____ one_pair():
            r.. ONE_PAIR + rank_of_card_with_highest_occurence()
        ____:
            r.. high_card()

    ___ straight_flush
        r.. straight() a.. flush()

    ___ straight
        r.. (l..(r..(m..(ranks), max(ranks) + 1)) __
                s..(ranks))

    ___ flush
        r.. l..(set(suits)) __ 1

    ___ four_of_a_kind
        r.. max(rank_occurences().values()) __ 4

    ___ full_house
        r.. three_of_a_kind() a.. one_pair()

    ___ three_of_a_kind
        r.. 3 __ l..(rank_occurences().values())

    ___ two_pair
        r.. 2 __ l..(rank_occurences().values()).c.. 2)

    ___ one_pair
        r.. 2 __ l..(rank_occurences().values())

    ___ high_card
        r.. max(ranks)

    ___ rank_occurences
        r.. {rank: ranks.c.. rank) ___ rank __ ranks}

    ___ rank_of_card_with_highest_occurence
        r.. max(rank_occurences(), key=rank_occurences().get)


c_ Card:
    FACE_CARDS = {"T": 10,
                  "J": 11,
                  "Q": 12,
                  "K": 13,
                  "A": 14}

    ___ - , inp):
        rank = numberify_face_cards(inp[0])
        suit = inp[1]

    ___ __str__
        r.. s..(rank) + suit

    @classmethod
    ___ numberify_face_cards(cls, rank):
        __ rank __ l..(cls.FACE_CARDS.k..
            r.. cls.FACE_CARDS[rank]
        r.. int(rank)


___ poker(inp):
    r.. Poker(inp).best_hand()
