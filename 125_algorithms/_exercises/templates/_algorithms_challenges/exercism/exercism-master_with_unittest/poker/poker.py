STRAIGHT_FLUSH = 800
FOUR_OF_A_KIND = 700
FULL_HOUSE = 600
FLUSH = 500
STRAIGHT = 400
THREE_OF_A_KIND = 300
TWO_PAIR = 200
ONE_PAIR = 100
HIGH_CARD = 0


class Poker:
    ___ __init__(self, hands):
        self.hands = [Hand(hand) ___ hand __ hands]

    ___ best_hand(self):
        r.. [hand.hand ___ hand, score __ l..(
            self.scores().items()) __ score __ self.best_score()]

    ___ best_score(self):
        r.. max(self.scores(), key=self.scores().get).score()

    ___ scores(self):
        r.. {hand: hand.score() ___ hand __ self.hands}


class Hand:
    ___ __init__(self, hand):
        self.hand = hand
        self.cards = [Card(card) ___ card __ hand]
        self.ranks = [card.rank ___ card __ self.cards]
        self.suits = [card.suit ___ card __ self.cards]

    ___ score(self):
        __ self.straight_flush():
            r.. STRAIGHT_FLUSH + self.high_card()
        ____ self.four_of_a_kind():
            r.. FOUR_OF_A_KIND + self.rank_of_card_with_highest_occurence()
        ____ self.full_house():
            r.. FULL_HOUSE + self.rank_of_card_with_highest_occurence()
        ____ self.flush():
            r.. FLUSH + self.high_card()
        ____ self.straight():
            r.. STRAIGHT + self.high_card()
        ____ self.three_of_a_kind():
            r.. THREE_OF_A_KIND + self.rank_of_card_with_highest_occurence()
        ____ self.two_pair():
            r.. TWO_PAIR + self.high_card()
        ____ self.one_pair():
            r.. ONE_PAIR + self.rank_of_card_with_highest_occurence()
        ____:
            r.. self.high_card()

    ___ straight_flush(self):
        r.. self.straight() and self.flush()

    ___ straight(self):
        r.. (l..(r..(m..(self.ranks), max(self.ranks) + 1)) __
                s..(self.ranks))

    ___ flush(self):
        r.. l..(set(self.suits)) __ 1

    ___ four_of_a_kind(self):
        r.. max(self.rank_occurences().values()) __ 4

    ___ full_house(self):
        r.. self.three_of_a_kind() and self.one_pair()

    ___ three_of_a_kind(self):
        r.. 3 __ l..(self.rank_occurences().values())

    ___ two_pair(self):
        r.. 2 __ l..(self.rank_occurences().values()).c.. 2)

    ___ one_pair(self):
        r.. 2 __ l..(self.rank_occurences().values())

    ___ high_card(self):
        r.. max(self.ranks)

    ___ rank_occurences(self):
        r.. {rank: self.ranks.c.. rank) ___ rank __ self.ranks}

    ___ rank_of_card_with_highest_occurence(self):
        r.. max(self.rank_occurences(), key=self.rank_occurences().get)


class Card:
    FACE_CARDS = {"T": 10,
                  "J": 11,
                  "Q": 12,
                  "K": 13,
                  "A": 14}

    ___ __init__(self, inp):
        self.rank = self.numberify_face_cards(inp[0])
        self.suit = inp[1]

    ___ __str__(self):
        r.. str(self.rank) + self.suit

    @classmethod
    ___ numberify_face_cards(cls, rank):
        __ rank __ l..(cls.FACE_CARDS.keys()):
            r.. cls.FACE_CARDS[rank]
        r.. int(rank)


___ poker(inp):
    r.. Poker(inp).best_hand()
