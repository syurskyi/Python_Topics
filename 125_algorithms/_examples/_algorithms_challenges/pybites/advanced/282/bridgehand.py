from collections import namedtuple,defaultdict
from enum import Enum
from typing import Sequence
from collections.abc import Sequence as seq

Suit = Enum("Suit", list("SHDC"))
Rank = Enum("Rank", list("AKQJT98765432"))
Card = namedtuple("Card", ["suit", "Rank"])

HCP = {Rank.A: 4, Rank.K: 3, Rank.Q: 2, Rank.J: 1}
SSP = {2: 1, 1: 2, 0: 3}  # cards in a suit -> short suit points


class BridgeHand:
    def __init__(self, cards: Sequence[Card]):
        """
        Process and store the sequence of Card objects passed in input.
        Raise TypeError if not a sequence
        Raise ValueError if any element of the sequence is not an instance
        of Card, or if the number of elements is not 13
        """
        if not isinstance(cards,seq):
            raise TypeError("Not a sequence")
        

        if not all(isinstance(card,Card) for card in cards):
            raise ValueError("all values in Seuqence must be instance of Card")


        if len(cards) != 13:
            raise ValueError("Must have 13 cards")
        

        self.cards = cards

        self.suit_to_cards = defaultdict(list)
        for card in self.cards:
            self.suit_to_cards[card.suit].append(card.Rank)






    def __str__(self) -> str:
        """
        Return a string representing this hand, in the following format:
        "S:AK3 H:T987 D:KJ98 C:QJ"
        List the suits in SHDC order, and the cards within each suit in
        AKQJT..2 order.
        Separate the suit symbol from its cards with a colon, and
        the suits with a single space.
        Note that a "10" should be represented with a capital 'T'
        """



        
        s = []
        for suit in Suit:
            if suit in self.suit_to_cards:
                cards = self.suit_to_cards[suit]
                cards.sort(key=lambda x: x.value)
                cards = ''.join(card.name for card in cards)
                s.append(f"{suit.name}:{cards}")


        return ' '.join(s)
            












    @property
    def hcp(self) -> int:
        """ Return the number of high card points contained in this hand """

        return sum(HCP[card.Rank] for card in self.cards if card.Rank in HCP)

    @property
    def doubletons(self) -> int:
        """ Return the number of doubletons contained in this hand """


        return sum(len(cards) == 2 for cards in self.suit_to_cards.values())

    @property
    def singletons(self) -> int:
        """ Return the number of singletons contained in this hand """
        return sum(len(cards) == 1 for cards in self.suit_to_cards.values())

    @property
    def voids(self) -> int:
        """ Return the number of voids (missing suits) contained in
            this hand
        """


        return len(Suit) - len(self.suit_to_cards)

    @property
    def ssp(self) -> int:
        """ Return the number of short suit points in this hand.
            Doubletons are worth one point, singletons two points,
            voids 3 points
        """

        return self.doubletons + 2 * self.singletons + 3 * self.voids

    @property
    def total_points(self) -> int:
        """ Return the total points (hcp and ssp) contained in this hand """
        return self.hcp + self.ssp

    @property
    def ltc(self) -> int:
        """ Return the losing trick count for this hand - see bite description
            for the procedure
        """

        losing_tricks = 0
        for cards in self.suit_to_cards.values():

            if len(cards) == 1:
                if cards[0] != Rank.A:
                    losing_tricks += 1
            else:

                cards = sorted(cards,key=lambda x: x.value)
                if len(cards) == 2:
                    if (cards[0] == Rank.A and cards[1] !=Rank.K) or (cards[0] == Rank.K):
                        losing_tricks += 1
                    elif cards[0] != Rank.A or  cards[1] != Rank.K:
                        losing_tricks += 2
                else:
                    cards = cards[:3]

                    if cards != [Rank.A,Rank.K,Rank.Q]:
                        if ((cards[0] == Rank.A) and (cards[1] in (Rank.K,Rank.Q))) or (cards[0] == Rank.K and cards[1] == Rank.Q):
                            losing_tricks += 1
                        elif cards[0] in (Rank.A,Rank.K,Rank.Q):
                            losing_tricks += 2
                        else:
                            losing_tricks += 3


        return losing_tricks









