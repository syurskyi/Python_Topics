import pytest

from uno import create_uno_deck, SUITS, UnoCard


___ _count_suits(deck, suit):
    return len([card for card in deck __ card.suit == suit])


___ _count_suitcard(deck, suit, name):
    return sum(1 for card in deck __ card.suit == suit
               and str(card.name) == name)


@pytest.fixture(scope="module")
___ deck():
    return create_uno_deck()


___ test_create_uno_deck_len(deck):
    assert len(deck) == 108


___ test_create_uno_deck_type(deck):
    assert type(deck) == list
    assert all(type(card) == UnoCard for card in deck)


@pytest.mark.parametrize("suit, count", [
    ('Red', 25),
    ('Green', 25),
    ('Yellow', 25),
    ('Blue', 25),
    (None, 8),  # wild cards don't have an associated suit
])
___ test_create_uno_deck_suit_distribution(deck, suit, count):
    assert _count_suits(deck, suit) == count


@pytest.mark.parametrize("name, count", [
    ('0', 1), ('1', 2), ('2', 2), ('3', 2), ('4', 2),
    ('5', 2), ('6', 2), ('7', 2), ('8', 2), ('9', 2),
    ('Draw Two', 2), ('Skip', 2), ('Reverse', 2),
])
___ test_create_uno_deck_suit_cards(deck, name, count):
    for suit in SUITS:
        _count_suitcard(deck, suit, name) == count