_______ pytest

____ uno _______ create_uno_deck, SUITS, UnoCard


___ _count_suits(deck, suit):
    r.. l..([card ___ card __ deck __ card.suit __ suit])


___ _count_suitcard(deck, suit, name):
    r.. s..(1 ___ card __ deck __ card.suit __ suit
               a.. s..(card.name) __ name)


@pytest.fixture(scope="module")
___ deck
    r.. create_uno_deck()


___ test_create_uno_deck_len(deck):
    ... l..(deck) __ 108


___ test_create_uno_deck_type(deck):
    ... t..(deck) __ l..
    ... a..(t..(card) __ UnoCard ___ card __ deck)


@pytest.mark.parametrize("suit, count", [
    ('Red', 25),
    ('Green', 25),
    ('Yellow', 25),
    ('Blue', 25),
    (N.., 8),  # wild cards don't have an associated suit
])
___ test_create_uno_deck_suit_distribution(deck, suit, count):
    ... _count_suits(deck, suit) __ count


@pytest.mark.parametrize("name, count", [
    ('0', 1), ('1', 2), ('2', 2), ('3', 2), ('4', 2),
    ('5', 2), ('6', 2), ('7', 2), ('8', 2), ('9', 2),
    ('Draw Two', 2), ('Skip', 2), ('Reverse', 2),
])
___ test_create_uno_deck_suit_cards(deck, name, count):
    ___ suit __ SUITS:
        _count_suitcard(deck, suit, name) __ count