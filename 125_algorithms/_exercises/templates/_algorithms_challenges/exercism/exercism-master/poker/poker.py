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
    ___ __init__(self, hands
        self.hands = [Hand(hand) for hand in hands]

    ___ best_hand(self
        r_ [hand.hand for hand, score in list(
            self.scores().items()) __ score __ self.best_score()]

    ___ best_score(self
        r_ max(self.scores(), key=self.scores().get).score()

    ___ scores(self
        r_ {hand: hand.score() for hand in self.hands}


class Hand:
    ___ __init__(self, hand
        self.hand = hand
        self.cards = [Card(card) for card in hand]
        self.ranks = [card.rank for card in self.cards]
        self.suits = [card.suit for card in self.cards]

    ___ score(self
        __ self.straight_flush(
            r_ STRAIGHT_FLUSH + self.high_card()
        ____ self.four_of_a_kind(
            r_ FOUR_OF_A_KIND + self.rank_of_card_with_highest_occurence()
        ____ self.full_house(
            r_ FULL_HOUSE + self.rank_of_card_with_highest_occurence()
        ____ self.flush(
            r_ FLUSH + self.high_card()
        ____ self.straight(
            r_ STRAIGHT + self.high_card()
        ____ self.three_of_a_kind(
            r_ THREE_OF_A_KIND + self.rank_of_card_with_highest_occurence()
        ____ self.two_pair(
            r_ TWO_PAIR + self.high_card()
        ____ self.one_pair(
            r_ ONE_PAIR + self.rank_of_card_with_highest_occurence()
        ____
            r_ self.high_card()

    ___ straight_flush(self
        r_ self.straight() and self.flush()

    ___ straight(self
        r_ (list(range(min(self.ranks), max(self.ranks) + 1)) __
                sorted(self.ranks))

    ___ flush(self
        r_ le.(set(self.suits)) __ 1

    ___ four_of_a_kind(self
        r_ max(self.rank_occurences().values()) __ 4

    ___ full_house(self
        r_ self.three_of_a_kind() and self.one_pair()

    ___ three_of_a_kind(self
        r_ 3 in list(self.rank_occurences().values())

    ___ two_pair(self
        r_ 2 __ list(self.rank_occurences().values()).count(2)

    ___ one_pair(self
        r_ 2 in list(self.rank_occurences().values())

    ___ high_card(self
        r_ max(self.ranks)

    ___ rank_occurences(self
        r_ {rank: self.ranks.count(rank) for rank in self.ranks}

    ___ rank_of_card_with_highest_occurence(self
        r_ max(self.rank_occurences(), key=self.rank_occurences().get)


class Card:
    FACE_CARDS = {"T": 10,
                  "J": 11,
                  "Q": 12,
                  "K": 13,
                  "A": 14}

    ___ __init__(self, inp
        self.rank = self.numberify_face_cards(inp[0])
        self.suit = inp[1]

    ___ __str__(self
        r_ str(self.rank) + self.suit

    @classmethod
    ___ numberify_face_cards(cls, rank
        __ rank in list(cls.FACE_CARDS.keys()):
            r_ cls.FACE_CARDS[rank]
        r_ int(rank)


___ poker(inp
    r_ Poker(inp).best_hand()
