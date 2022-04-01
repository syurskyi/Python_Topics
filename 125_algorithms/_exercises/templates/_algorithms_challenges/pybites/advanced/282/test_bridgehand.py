____ dataclasses _______ dataclass, field
____ r__ _______ shuffle
____ typing _______ List

_______ p__

____ bridgehand _______ Suit, Rank, Card, BridgeHand


@dataclass
c_ TestHand:
    card_string: s..
    doubletons: i..
    singletons: i..
    voids: i..
    hcp: i..
    ssp: i..
    total_points: i..
    ltc: i..
    card_list: List[Card] = field(init=F..)

    ___ __post_init__
        """ Generate actual list of Card instances from card_string """
        card_list    # list
        ___ suit_holding __ card_string.s.. :
            suit = Suit[suit_holding[0]]
            ___ rank __ suit_holding[2:]:
                card = Card(suit, Rank[rank])
                card_list.a..(card)
        shuffle(card_list)


test_hands = [
    TestHand("S:AKJ H:QJT9 D:5432 C:AK", 1, 0, 0, 18, 1, 19, 6),
    TestHand("S:A76 H:KT75 D:KQ2 C:AK8", 0, 0, 0, 19, 0, 19, 6),
    TestHand("S:AKQJT98765432", 0, 0, 3, 10, 9, 19, 0),
    TestHand("S:5432 H:5432 D:543 C:32", 1, 0, 0, 0, 1, 1, 11),
    TestHand("S:K642 H:Q985 D:AT64 C:4", 0, 1, 0, 9, 2, 11, 7),
    TestHand("S:KQ3 H:Q76 D:J43 C:J987", 0, 0, 0, 9, 0, 9, 9),
    TestHand("S:A64 H:72 D:KJ8542 C:AJ", 2, 0, 0, 13, 2, 15, 7),
    TestHand("S:AT4 H:86 D:A984 C:AKT7", 1, 0, 0, 15, 1, 16, 7),
    TestHand("S:J972 H:9 D:98742 C:T54", 0, 1, 0, 1, 2, 3, 10),
    TestHand("S:9854 H:K43 D:Q5 C:9873", 1, 0, 0, 5, 1, 6, 10),
    TestHand("S:KT943 H:T63 D:JT5 C:97", 1, 0, 0, 4, 1, 5, 10),
    TestHand("S:T9732 H:J86 D:K93 C:86", 1, 0, 0, 4, 1, 5, 10),
    TestHand("S:KT8 H:94 D:AJT4 C:6532", 1, 0, 0, 8, 1, 9, 9),
    TestHand("S:AQT92 H:J763 D:763 C:6", 0, 1, 0, 7, 2, 9, 8),
    TestHand("S:AK94 H:K743 D:AKT C:72", 1, 0, 0, 17, 1, 18, 6),
    TestHand("S:A974 D:AK94 C:QJ932", 0, 0, 1, 14, 3, 17, 5),
    TestHand("S:J873 H:KJ62 D:A96 C:K8", 1, 0, 0, 12, 1, 13, 8),
    TestHand("S:T732 H:T2 D:JT8 C:AK96", 1, 0, 0, 8, 1, 9, 9),
    TestHand("S:KT H:AK975 D:QJT2 C:KJ", 2, 0, 0, 17, 2, 19, 5),
    TestHand("S:KJT97 H:AQ843 D:86 C:5", 1, 1, 0, 10, 3, 13, 6),
]

hand_pairs = [(BridgeHand(hand.card_list), hand) ___ hand __ test_hands]

malformed_hands = [
    TestHand("S:AKJ H:QJT9 D:765432 C:AK", 1, 0, 0, 18, 1, 19, 6),
    TestHand("S:A H:K D:Q2 C:K8", 0, 0, 0, 19, 0, 19, 6),
]


___ test_null_cards
    w__ p__.r.. T..
        BridgeHand(N..)


___ test_wrong_type
    w__ p__.r.. T..
        BridgeHand(42)


___ test_wrong_cards
    w__ p__.r..(ValueError):
        BridgeHand([Card(Suit.S, Rank.A)] + [N..] * 12)


@p__.m__.p..("hand", malformed_hands)
___ test_wrong_number_of_cards(hand):
    w__ p__.r..(ValueError):
        BridgeHand(hand.card_list)


@p__.m__.p..("bridge_hand, test_hand", hand_pairs)
___ test_str(bridge_hand, test_hand):
    ... s..(bridge_hand) __ test_hand.card_string


@p__.m__.p..("bridge_hand, test_hand", hand_pairs)
___ test_doubletons(bridge_hand, test_hand):
    ... bridge_hand.doubletons __ test_hand.doubletons


@p__.m__.p..("bridge_hand, test_hand", hand_pairs)
___ test_hcp(bridge_hand, test_hand):
    ... bridge_hand.hcp __ test_hand.hcp


@p__.m__.p..("bridge_hand, test_hand", hand_pairs)
___ test_singletons(bridge_hand, test_hand):
    ... bridge_hand.singletons __ test_hand.singletons


@p__.m__.p..("bridge_hand, test_hand", hand_pairs)
___ test_voids(bridge_hand, test_hand):
    ... bridge_hand.voids __ test_hand.voids


@p__.m__.p..("bridge_hand, test_hand", hand_pairs)
___ test_ssp(bridge_hand, test_hand):
    ... bridge_hand.ssp __ test_hand.ssp


@p__.m__.p..("bridge_hand, test_hand", hand_pairs)
___ test_total_points(bridge_hand, test_hand):
    ... bridge_hand.total_points __ test_hand.total_points


@p__.m__.p..("bridge_hand, test_hand", hand_pairs)
___ test_ltc(bridge_hand, test_hand):
    ... bridge_hand.ltc __ test_hand.ltc